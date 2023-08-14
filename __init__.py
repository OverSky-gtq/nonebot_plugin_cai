import json

from characterai import PyAsyncCAI
from nonebot import get_driver
from nonebot.params import CommandArg
from nonebot.plugin import on_command
from nonebot_plugin_guild_patch import GuildMessageEvent, Message, MessageSegment

client = ''
char = ''
history_id = ''
tgt = ''
config = {}
channel_on = [614317740]
# 读取JSON文件
with open('./plugins/nonebot_plugin_cai/config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


async def updataChat():
    global client
    global char
    global history_id
    global tgt
    chat = await client.chat.get_chat(char)

    history_id = chat['external_id']
    participants = chat['participants']

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']


driver = get_driver()
re = on_command('ep', aliases={'re'})
change = on_command('change')
newchat = on_command('newchat')
menu = on_command('menu')
delete = on_command('roll')

@driver.on_startup
async def do_something():
    global client
    global char
    global history_id
    global tgt
    client = PyAsyncCAI('89d650a717eb148ac5a55639a0f56f3c19a22ef7')
    await client.start()
    char = 'ZWJkqbFXPx1toC_cOxnGkT6KTwezTvcKDTGP6EfTfHo'

    # Save tgt and history_external_id 
    # to avoid making a lot of requests
    chat = await client.chat.get_chat(char)

    history_id = chat['external_id']
    participants = chat['participants']

    # In the list of "participants",
    # a character can be at zero or in the first place

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']


@menu.handle()
async def _(event: GuildMessageEvent):
    if event.channel_id in channel_on:
        global config
        content = ''
        for key in config.keys():
            content += str(key) + '\n'
        await menu.finish(Message(content))

@re.handle()
async def _(event: GuildMessageEvent, args: Message = CommandArg()):
    if event.channel_id in channel_on:
        if reply := args.extract_plain_text():
            global client
            global char
            global history_id
            global tgt

            data = await client.chat.send_message(
                char, reply, history_external_id=history_id, tgt=tgt
            )

            # name = data['src_char']['participant']['name']
            text = data['replies'][0]['text']
            await re.send(MessageSegment.at(event.user_id) + Message(text))
        else:
            await re.finish("内容不可为空白")


@newchat.handle()
async def _(event: GuildMessageEvent, args: Message = CommandArg()):
    if event.channel_id in channel_on:
        role = args.extract_plain_text().strip()
        global client
        global char
        global config
        temp = char
        if role:
            try:
                char = config[role]
            except KeyError:
                pass
        chat = await client.chat.new_chat(char)
        welcome = chat['messages'][0]['text']

        await newchat.send(MessageSegment.at(event.user_id) + Message(welcome))
        if temp != char:
            await updataChat()


@change.handle()
async def _(event: GuildMessageEvent, args: Message = CommandArg()):
    if event.channel_id in channel_on:
        if role := args.extract_plain_text().strip():
            global char
            global config
            try:
                char = config[role]
            except KeyError:
                await change.finish(MessageSegment.at(event.user_id) + Message("不存在此角色"))
            await updataChat()

            await change.finish(MessageSegment.at(event.user_id) + Message("切换成功"))
        else:
            await change.finish("内容不可为空白")

@delete.handle()
async def _(event: GuildMessageEvent):
    if event.channel_id in channel_on:
        global client
        global char
        global history_id
        uuids_to_delete = []

        history = await client.chat.get_history(char)

        uuids_to_delete.append(history['messages'][-1]['uuid'])
        # uuids_to_delete.append(history['messages'][-2]['uuid'])

        await client.chat.delete_message(history_id, uuids_to_delete)
        await delete.finish(MessageSegment.at(event.user_id) + Message("回溯成功"))