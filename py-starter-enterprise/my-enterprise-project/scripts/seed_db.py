#!/usr/bin/env python3
"""Database seeding script."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from my_enterprise_project.db.session import engine
from my_enterprise_project.db.models import Base, User, Task


def seed_database():
    """Seed the database with sample data."""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create a session
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).first():
            print("Database already seeded.")
            return
        
        # Create sample users
        users = [
            User(name="John Doe", email="john@example.com"),
            User(name="Jane Smith", email="jane@example.com"),
        ]
        
        for user in users:
            db.add(user)
        
        db.commit()
        
        # Create sample tasks
        tasks = [
            Task(title="Sample Task 1", description="First sample task"),
            Task(title="Sample Task 2", description="Second sample task", completed=True),
        ]
        
        for task in tasks:
            db.add(task)
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
