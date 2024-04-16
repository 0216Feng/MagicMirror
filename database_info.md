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
TID INTEGER PRIMARY KEY NOT NULL,
Brand TEXT NOT NULL,
Type TEXT NOT NULL,
Expire TEXT NOT NULL,
Description Text);

