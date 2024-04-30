# Database document

## courseInfo

|   Items    |   CID   |    Name    | Time | Location | Week | Description |
| :--------: | :-----: | :--------: | :--: | :------: | :--: | :---------: |
| Attributes | int, PK | Title, str | str  |   str    | str  |     str     |

courseInfo表中CID为PRIMARY KEY，用于唯一指定一个项。Name表示课程的显示的名字，Time表示发生的时间段，Location表示课程的地点(非必要)，Week表示日程重复的时间(非必要)，Description表示备注和其它描述(非必要)。

CREATE TABLE courseInfo (
CID INTEGER PRIMARY KEY NOT NULL,
Name TEXT NOT NULL,
Time TEXT NOT NULL,
Location TEXT,
Week TEXT,
Description Text);

## scheduleInfo

|   Items    |   SID   |    Name    | Time | Location | Description |
| :--------: | :-----: | :--------: | :--: | :------: | :---------: |
| Attributes | int, PK | Title, str | str  |   str    |     str     |

scheduleInfo表中SID为PRIMARY KEY，用于唯一指定一个项。Name表示该日程的显示的名字，Time表示发生的时间，Location表示日程的地点(非必要)，Description表示备注和其它描述(非必要)。

CREATE TABLE scheduleInfo (
SID INTEGER PRIMARY KEY NOT NULL,
Name TEXT NOT NULL,
Time TEXT NOT NULL,
Location TEXT,
Description Text);

## tipsInfo
|   Items    |   TID   | Published |   Title    | Description |
| :--------: | :-----: | :-------: | :--------: | :---------: |
| Attributes | int, PK |    str    |    str     |     str     |

tipsInfo表中TID为PRIMARY KEY，用于唯一指定一个项。Title表示该日程的显示的名字，Time表示发布的时间，Description表示备注内容和其它描述。

CREATE TABLE tipsInfo (
TID INTEGER PRIMARY KEY NOT NULL,
Published TEXT NOT NULL,
Title TEXT NOT NULL,
Description Text NOT NULL);

## careInfo
|   Items    |   BID   |  Brand  |   Type   |   Expire  | Description |
| :--------: | :-----: | :-----: | :------: | :-------: | :---------: |
| Attributes | int, PK |   str   |   str    |    str    |     str     |

careInfo表中BID为PRIMARY KEY，用于唯一指定一个项。Brand表示个人护理产品的品牌，Type表示个人护理产品的类型，Expire表示过期的时间，Description表示备注内容和其它描述。

CREATE TABLE careInfo (
BID INTEGER PRIMARY KEY NOT NULL,
Brand TEXT NOT NULL,
Type TEXT NOT NULL,
Expire TEXT NOT NULL,
Description Text);

## galleryInfo

|   Items    |   GID   |  Address  |
| :--------: | :-----: | :-------: |
| Attributes | int, PK |    str    |

galleryInfo表中GID为PRIMARY KEY，用于唯一指定一个项。Address表示图片文件所在的路径。

CREATE TABLE galleryInfo (
GID INTEGER PRIMARY KEY NOT NULL,
Address TEXT NOT NULL);

## statusInfo
|   Items    |   Item   |  State  |
| :--------: | :------: | :-----: |
| Attributes | str, PK  |  int    |

该表用于检测某个组件时候开启。statusInfo表中Item为PRIMARY KEY，用于唯一指定一个项。State为其状态，其值为true(1)/false(0)。

CREATE TABLE statusInfo (
Item TEXT PRIMARY KEY NOT NULL,
State INTERGER NOT NULL);

初始状态下：
```
Weather|1
News|0
Course|0
Schedule|0
Tips|0
Care|0
Gallery|0
```