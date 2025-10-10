"""
目标检测 ML API

使用 YOLOv8 进行目标检测
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from ultralytics import YOLO
from pathlib import Path

# 创建 FastAPI 应用
app = FastAPI(
    title="ML API - YOLOv8",
    description="目标检测服务",
    version="{{ cookiecutter.version }}",
)

# 加载模型
MODEL_PATH = Path("models/yolov8n.pt")
model = None

@app.on_event("startup")
async def load_model():
    """启动时加载模型"""
    global model
    if MODEL_PATH.exists():
        model = YOLO(str(MODEL_PATH))
        print(f"✅ 模型加载成功: {MODEL_PATH}")
    else:
        print(f"⚠️  模型文件不存在: {MODEL_PATH}")
        print("📥 正在下载默认模型...")
        model = YOLO("yolov8n.pt")  # 自动下载
        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        model.save(str(MODEL_PATH))

@app.get("/")
async def root():
    """根路径"""
    return {
        "success": True,
        "message": "目标检测 ML API",
        "model": "YOLOv8n",
        "status": "ready" if model else "loading",
    }

@app.get("/health")
async def health():
    """健康检查"""
    return {
        "success": True,
        "status": "healthy" if model else "unhealthy",
    }

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    """
    目标检测
    
    Args:
        file: 上传的图片文件
        
    Returns:
        检测结果，包括物体类别、置信度和边界框
    """
    if not model:
        raise HTTPException(status_code=503, detail="模型未加载")
    
    try:
        # 读取图片
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise HTTPException(status_code=400, detail="无效的图片文件")
        
        # 执行推理
        results = model(img)
        
        # 解析结果
        detections = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                detections.append({
                    "class": model.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy[0].tolist(),  # [x1, y1, x2, y2]
                })
        
        return {
            "success": True,
            "data": {
                "detections": detections,
                "count": len(detections),
            },
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

