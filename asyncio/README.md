# asyncio

## install
built-in, no installation required

## import
import asyncio

## tips
* some functions are coroutine, you can get call them by __loop.run_until_complete(coro)__
* to run more then one tasks, use __asyncio.ensure_future()__ to create all tasks, then call __loop.run_forever()__
* to wait tasks complete (and get results), use __.gather()__ / __.wait()__, see https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait
