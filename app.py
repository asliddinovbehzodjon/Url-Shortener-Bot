from aiogram import Bot,Dispatcher,executor,types
import requests
import json
token='Sizning API tokeningiz'
bot=Bot(token=token)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    pic=open('pic.jpeg','rb')
    caption='<b>Assalomu aleykum!Botga Xush kelibsiz!</b>'+'\n'+'<b>Bot sizga uzun url manzilni qisqartirib beradi!</b>'
    await bot.send_photo(message.chat.id,pic,caption=caption,parse_mode='html')
@dp.message_handler(content_types=['text'])
async def asosiy(message:types.Message):
    text=message.text
    key='Cutly API key'
    import requests
    link=text
    url='http://cutt.ly/api/api.php?key={}&short={}'.format(key,text)
    r = requests.get(url)
    a=json.loads(r.text)
    shortlink=a['url']['shortLink']
    short='https://github.com/public-apis/public-apis#development'
    qrcode='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={}'.format(text)
    caption='Qisqartirilgan url manzil: '+shortlink+'\n'+'Asl url manzil: '+text+'\n'+'Bizning bot: @shortenurl_robot'
    await bot.send_photo(message.chat.id,qrcode,caption=caption)

if __name__=='__main__':
    executor.start_polling(dp)
