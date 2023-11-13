# scheduleBot
Bot for schedule!
===========

**Commands**

*1. /start - starts bot and commands*

*2. /notify - enable and disable notifications from bot*

*3. /donate - support dev with your donate*

## Library: aiogram
-----------
```
imports: aiogram, aiogram.types, datetime, config (token), apscheduler

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
```
