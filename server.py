from aiohttp import web
import aiohttp_jinja2
from core import Assistant
import demo_commands

@aiohttp_jinja2.template('index.html')
async def handle(request):
    return {}

@aiohttp_jinja2.template('feedback.html')
async def user_input(request):
	data = await request.post()
	user_input = data['user_input']
	assistant = demo_commands.commands(Assistant())
	output = assistant.execute(user_input)
	return {'user_input': user_input, 'output': output}

async def event_trigger(request):
	data = await request.json()
	print(data)
	return web.Response()

app = web.Application()
app.router.add_route('GET', '/', handle)
app.router.add_route('POST', '/user_input', user_input)
app.router.add_route('POST', '/event_trigger', event_trigger)
aiohttp_jinja2.setup(app,
    loader=aiohttp_jinja2.jinja2.FileSystemLoader('./'))

web.run_app(app)