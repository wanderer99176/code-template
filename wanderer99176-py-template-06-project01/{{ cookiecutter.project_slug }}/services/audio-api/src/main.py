"""
音频处理 API

使用 Fast-Whisper 进行语音转文字
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from faster_whisper import WhisperModel
import tempfile
from pathlib import Path

# 创建 FastAPI 应用
app = FastAPI(
    title="Audio API - Whisper",
    description="音频转录服务",
    version="{{ cookiecutter.version }}",
)

# 加载模型
model = None
MODEL_SIZE = "base"  # tiny, base, small, medium, large

@app.on_event("startup")
async def load_model():
    """启动时加载模型"""
    global model
    print(f"📥 正在加载 Whisper 模型: {MODEL_SIZE}")
    model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")
    print(f"✅ 模型加载完成")

@app.get("/")
async def root():
    """根路径"""
    return {
        "success": True,
        "message": "音频转录 API",
        "model": f"Whisper-{MODEL_SIZE}",
        "status": "ready" if model else "loading",
    }

@app.get("/health")
async def health():
    """健康检查"""
    return {
        "success": True,
        "status": "healthy" if model else "unhealthy",
    }

@app.post("/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    language: str = "zh",
):
    """
    音频转录
    
    Args:
        file: 上传的音频文件
        language: 语言代码 (zh, en, ja, etc.)
        
    Returns:
        转录文本和详细信息
    """
    if not model:
        raise HTTPException(status_code=503, detail="模型未加载")
    
    try:
        # 保存临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name
        
        # 执行转录
        segments, info = model.transcribe(
            tmp_path,
            language=language,
            beam_size=5,
        )
        
        # 收集结果
        transcription = []
        full_text = []
        
        for segment in segments:
            transcription.append({
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip(),
            })
            full_text.append(segment.text.strip())
        
        # 删除临时文件
        Path(tmp_path).unlink()
        
        return {
            "success": True,
            "data": {
                "text": " ".join(full_text),
                "segments": transcription,
                "language": info.language,
                "duration": info.duration,
            },
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

