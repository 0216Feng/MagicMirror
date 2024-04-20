from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from databases import Database
from pydantic import BaseModel
import os
import shutil
import uuid

database = Database("sqlite:///database.db")
app = FastAPI()
app.mount("/src", StaticFiles(directory="src"), name="src")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Database connection
async def database_connection():
    await database.connect()

async def database_disconnection():
    await database.disconnect()

# Show infomation of database
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open('src/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.get("/getCourses")
async def getCourses():
    await database_connection()
    
    query = "SELECT * FROM courseInfo"
    course = await database.fetch_all(query=query)
    query = "SELECT COUNT(*) FROM courseInfo"
    count = await database.fetch_all(query=query)
    await database_disconnection()
    
    return {
        "status": 200,
        "course": course,
        "count": count[0][0]
    }

@app.get("/getSchedules")
async def getSchedules():
    await database_connection()
    
    query = "SELECT * FROM scheduleInfo"
    schedule = await database.fetch_all(query=query)
    query = "SELECT COUNT(*) FROM scheduleInfo"
    count = await database.fetch_all(query=query)
    await database_disconnection()
    
    return {
        "status": 200,
        "schedule": schedule,
        "count": count[0][0]
    }

@app.get("/getTips")
async def getTips():
    await database_connection()
    
    query = "SELECT * FROM tipsInfo"
    tip = await database.fetch_all(query=query)
    query = "SELECT COUNT(*) FROM tipsInfo"
    count = await database.fetch_all(query=query)
    
    await database_disconnection()
    
    return {
        "status": 200,
        "tip": tip,
        "count": count[0][0]
    }

@app.get("/getHealthcare")
async def getHealthcare():
    await database_connection()
    
    query = "SELECT * FROM careInfo"
    care = await database.fetch_all(query=query)
    query = "SELECT COUNT(*) FROM careInfo"
    count = await database.fetch_all(query=query)
    
    await database_disconnection()
    
    return {
        "status": 200,
        "care": care,
        "count": count[0][0]
    }

@app.get("/getGallery")
async def getGallery():
    await database_connection()
    
    query = "SELECT * FROM galleryInfo"
    care = await database.fetch_all(query=query)
    query = "SELECT COUNT(*) FROM galleryInfo"
    count = await database.fetch_all(query=query)
    
    await database_disconnection()
    
    return {
        "status": 200,
        "gallery": care,
        "count": count[0][0]
    }

@app.get("/getStatus")
async def getStatus():
    await database_connection()
    
    query = "SELECT * FROM statusInfo"
    items = await database.fetch_all(query=query)
    
    await database_disconnection()
    
    return {
        "status": 200,
        "Weather": items[0][1],
        "News": items[1][1],
        "Course": items[2][1],
        "Schedule": items[3][1],
        "Tips": items[4][1],
        "Care": items[5][1],
        "Gallery": items[6][1]
    }

# Add infomation of database
class Courseinfo(BaseModel):
    title: str
    description: str
    week: str
    time: str
    location: str
    
class Scheduleinfo(BaseModel):
    title: str
    description: str
    time: str
    location: str

class Tipsinfo(BaseModel):
    title: str
    description: str
    published: str
    
class Careinfo(BaseModel):
    brand: str
    type: str
    expire: str
    description: str

@app.post("/addCourse")
async def addCourse(request: Courseinfo):
    title = request.title
    description = request.description
    week = request.week
    time = request.time
    location = request.location
    
    await database_connection()
    
    if title == "" or time == "":
        return {
            "status": 400,
            "message": "Missing some information."
        }
    
    query = "SELECT MAX(CID) + 1 FROM courseInfo"
    cid = await database.fetch_one(query=query)
    if cid[0] is None:
        cid = 1
    else:
        cid = cid[0]
    
    query = "INSERT INTO courseInfo (CID, Name, Time, Location, Week, Description) VALUES (:cid, :name, :time, :location, :week, :description)"
    await database.execute(query=query, values={
        "cid": cid,
        "name": title,
        "time": time,
        "location": location,
        "week": week,
        "description": description})
    
    return {
        "status": 200,
        "message": "Success add course."
    }

@app.post("/addSchedule")
async def addSchedule(request: Scheduleinfo):
    title = request.title
    description = request.description
    time = request.time
    location = request.location
    
    await database_connection()
    
    if title == "" or time == "":
        return {
            "status": 400,
            "message": "Missing some information."
        }
    
    query = "SELECT MAX(SID) + 1 FROM scheduleInfo"
    sid = await database.fetch_one(query=query)
    if sid[0] is None:
        sid = 1
    else:
        sid = sid[0]
    
    query = "INSERT INTO scheduleInfo (SID, Name, Time, Location, Description) VALUES (:sid, :name, :time, :location, :description)"
    await database.execute(query=query, values={
        "sid": sid,
        "name": title,
        "time": time,
        "location": location,
        "description": description})
    
    
    return {
        "status": 200,
        "message": "Success add schedule."
    }

@app.post("/addTips")
async def addTips(request: Tipsinfo):
    title = request.title
    description = request.description
    published = request.published
    
    await database_connection()
    
    if title == "" or description == "" or published == "":
        return {
            "status": 400,
            "message": "Missing some information."
        }
    
    query = "SELECT MAX(TID) + 1 FROM tipsInfo"
    tid = await database.fetch_one(query=query)
    if tid[0] is None:
        tid = 1
    else:
        tid = tid[0]
    
    query = "INSERT INTO tipsInfo (TID, Published, Title, Description) VALUES (:tid, :published, :title, :description)"
    await database.execute(query=query, values={
        "tid": tid,
        "published": published,
        "title": title,
        "description": description})
    
    return {
        "status": 200,
        "message": "Success add tips."
    }
@app.post("/addHealthcare")
async def addHealthcare(request: Careinfo):
    brand = request.brand
    type = request.type
    expire = request.expire
    description = request.description
    
    await database_connection()
    
    if brand == "" or type == "" or expire == "":
        return {
            "status": 400,
            "message": "Missing some information."
        }
    
    query = "SELECT MAX(Bid) + 1 FROM careInfo"
    bid = await database.fetch_one(query=query)
    if bid[0] is None:
        bid = 1
    else:
        bid = bid[0]
    
    query = "INSERT INTO careInfo (BID, Brand, Type, Expire, Description) VALUES (:bid, :brand, :type, :expire, :description)"
    await database.execute(query=query, values={
        "bid": bid,
        "brand": brand,
        "type": type,
        "expire": expire,
        "description": description})
    
    return {
        "status": 200,
        "message": "Success add healthcare."
    }

@app.post("/addGallery")
async def addGallery(file: UploadFile = File(...)):
    type = os.path.splitext(file.filename)[1].replace(".", "")
    name = str(uuid.uuid4()) + "." + type
    path = f"./assets/{name}"
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        data = await file.read()
        f.write(data)
        shutil.copyfileobj(file.file, f)

    await database_connection()
    
    query = "SELECT MAX(GID) + 1 FROM galleryInfo"
    gid = await database.fetch_one(query=query)
    if gid[0] is None:
        gid = 1
    else:
        gid = gid[0]
    
    path = path.replace("./assets/", "/assets/")
    query = "INSERT INTO galleryInfo (GID, Address) VALUES (:gid, :address)"
    await database.execute(query=query, values={"gid": gid, "address": path})
    
    await database_disconnection()
    return {
        "status": 200,
        "message": "Success add gallery."
    }


# Change status
class Statusinfo(BaseModel):
    item: str
    state: int
    
@app.post("/changeStatus")
async def changeStatus(request: Statusinfo):
    item = request.item
    state = request.state
    
    await database_connection()
    
    query = "UPDATE statusInfo SET State = :state WHERE Item = :item"
    await database.execute(query=query, values={"item": item, "state": state})
    
    await database_disconnection()
    return {
        "status": 200,
        "message": "Success change status."
    }

# Delete
class DeleteCourseinfo(BaseModel):
    cid: int
class DeleteScheduleinfo(BaseModel):
    sid: int
class DeleteTipsinfo(BaseModel):
    tid: int
class DeleteCareinfo(BaseModel):
    bid: int
class DeleteGalleryinfo(BaseModel):
    gid: int

@app.post("/deleteCourse")
async def deleteCourse(request: DeleteCourseinfo):
    cid = request.cid
    await database_connection()
    
    query = "DELETE FROM courseInfo WHERE CID = :cid"
    await database.execute(query=query, values={"cid": cid})
    
    await database_disconnection()
    return {
        "status": 200,
        "message": "Success delete course."
    }

@app.post("/deleteSchedule")
async def deleteSchedule(request: DeleteScheduleinfo):
    sid = request.sid
    await database_connection()
    
    query = "DELETE FROM scheduleInfo WHERE SID = :sid"
    await database.execute(query=query, values={"sid": sid})
    
    await database_disconnection()
    
    return {
        "status": 200,
        "message": "Success delete schedule."
    
    }

@app.post("/deleteTips")
async def deleteTips(request: DeleteTipsinfo):
    tid = request.tid
    await database_connection()
    
    query = "DELETE FROM tipsInfo WHERE TID = :tid"
    await database.execute(query=query, values={"tid": tid})
    
    await database_disconnection()
    return {
        "status": 200,
        "message": "Success delete tips."
    }

@app.post("/deleteCare")
async def deleteCare(request: DeleteCareinfo):
    bid = request.bid
    await database_connection()
    
    query = "DELETE FROM careInfo WHERE Bid = :bid"
    await database.execute(query=query, values={"bid": bid})
    
    await database_disconnection()
    return {
        "status": 200,
        "message": "Success delete healthcare."
    }

@app.post("/deleteGallery")
async def deleteGallery(request: DeleteGalleryinfo):
    gid = request.gid
    await database_connection()
    
    query = "SELECT Address FROM galleryInfo WHERE GID = :gid"
    path = await database.fetch_one(query=query, values={"gid": gid})
    path = path[0].replace("/assets/", "./assets/")
    os.remove(path)
    
    query = "DELETE FROM galleryInfo WHERE GID = :gid"
    await database.execute(query=query, values={"gid": gid})
    
    await database_disconnection()
    
    return {
        "status": 200,
        "message": "Success delete gallery."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
