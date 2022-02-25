from pyrogram import Client,filters
from pyrogram.types import Message
from pyrogram.types import ChatPermissions
from pyromod import listen
import time
import asyncio
import random
say = ["کیومرث","قربون"]
animation_chars = [
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
    "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",]
admins = {}
stickers = ["CAACAgQAAxkBAALssGH3Ggi7GQu3VkYJ7N3nutUqjMQwAALrCwACBaZBUyDiEYu5F0b5IwQ","CAACAgQAAxkBAALstGH3GiZwvaF6-wN4r2AKYEujxU5jAAJ_CgACfiRBU6xhs-cagfmaIwQ","CAACAgQAAxkBAALsuGH3Gj7lIt2E9kaBhD7zxfcAAdICYgACMAsAAglfQVMwfZVKk_MUrCME","CAACAgQAAxkBAALsvGH3GlkoGqBFkDpGW0ZGD-yFUljHAALmCAACRPdBU_FTWtCfl3gwIwQ"]
api_id = 19504232
api_hash = "014607e14241d2da92b94b61a5e8d7ec"
fosh = ["کون","کیر","کص","ممه","کوبص","کوص","کونی","کیری","جنده","گاییدم","گایی","مادرتو","بی ناموس","کوصه","f"]
user_fosh = {}
cry_mute_admin = ["ادمین جون فحش نده","داش فحش نده","استغفرالله bro","ادمین فحش نده","متاسفانه به ادمین نمیتونم ایراد بگیرم","ایتس حرام بِرادِر"]
muted_user = []
ghazvin_fish = []
muted_dog_user = {}
list_adab_group_id = []
sticker_ekhtar_fosh = ["CAACAgUAAxkBAALtNmH5gYVGNgABG6HBFFnaPmrBQSxKhQACWQEAAq_D6FeE0ZO20sWgNiME","CAACAgUAAxkBAALtOmH5gauRTGapxkFO4yVSaQABnAL-JwAC-wEAAlkY6VfJ0fezYp8uIyME","CAACAgUAAxkBAALtPmH5gdiVKymknZj0DOoqGJfOi6Y9AALuAQAChdHpV-0RMEBGFX7PIwQ"]
dog_fosh = ["داش گلم دوج بهت میگه فحش نده","یک ستاره شدی تا پنج ستاره جا داری","یک ستاره شدی فحش بدی عواقب داره","فحش نده","فحش نده این فقط ی اخطار بود دفعه بعد بد تره"]
i_dont_know = [""]
hap_hap = ["جانم دا","بله پسرم","چیزی میخواهی؟","بله ک*ر قهوه ای","چیزی میخواستی ک*ر نارنجی؟","جونم ک*ر پرتقالی","به داداش ک*ر خاکستری","","بلی چیزی شده؟"]
sticker_hap_hap = ["CAACAgUAAxkBAALyLGIILhXAo90NP7jK41V5Kf3mMlQLAALwAgACNuTpV8AneJuiuZSxIwQ","CAACAgUAAxkBAALyMGIILi9xCMoaMYrsvHUtEj7H-lX8AAJGAgACwCzoVwpFvctKddCfIwQ","CAACAgUAAxkBAALyWGIILwXgAxLztdOfAkDV7-Xk9of8AAJFAQACZ5npV6-tyvexa9-gIwQ","CAACAgUAAxkBAALyXGIILzNIK6fdExZfZUWm_ufAqndnAAKgAQACZ9ToV7eUmIOAlh7VIwQ","CAACAgUAAxkBAALyYGIIL0PMeXp9s7pSoCqB-npSMxs1AALuAQAChdHpV-0RMEBGFX7PIwQ","CAACAgUAAxkBAALyRGIILuAZOcZgqhucBexf2TsjsvPxAAJMAQAClyXpV9cB94ZrhHJoIwQ","CAACAgUAAxkBAALyPGIILr1YYRVZlXxHGvY3AmFLni69AAKkAQACUxvpVzhDzS2PtFiNIwQ","CAACAgUAAxkBAALyOGIILqM32YTDmCzrf4KUNG2CxY1lAAJuAgAC2XLoVzSB8M7N1mHiIwQ"]
spoilgap = []
list_police = ["عزیزم ادب خاموشه","ادب خاموشه پسرم","باور کن خاموشه","خاموشه","خاموشه"]
bot = Client("newpupppp",api_id,api_hash)
azl_bot = []
kosdar = []
@bot.on_message()
async def action(cli:Client, m:Message):
    word = m.text
    grop = m.chat.id
    msg_id = m.message_id
    ch_id = m.from_user.username
    user_id = m.from_user.id
    if word == "قطر کسم":
        gap_kos = grop
        user_kos = user_id
        kos_msg = msg_id
        await bot.send_message(gap_kos,"وای داش واقعا زدی قطر کسم؟ یادم میمونه",reply_to_message_id=kos_msg)
        kosdar.append(user_kos)
    if word == "سایز کیرم":
        userkir = user_id
        gap_size = grop
        msg_size = msg_id
        if userkir in kosdar:
            await bot.send_message(gap_size,"شما کیر نداری یادت رفته؟",reply_to_message_id=msg_size)
            await action()
        number_dick = random.randint(1,100)
        if number_dick == 100:
            await bot.send_message(gap_size,"🎉بیشترین طول کیر برای شماست ۱۰۰ 🎉",reply_to_message_id=msg_size)
        if number_dick < 10:
            await bot.send_message(gap_size,"شما کیر نداری از دستور قطر کسم استفاده کن",reply_to_message_id=msg_size)
        else:
            await bot.send_message(gap_size,f"سایز کیر شما = {number_dick}",reply_to_message_id=msg_size)
    if word == "brain":
        editm = msg_id+1
        gape = grop
        await bot.send_message(gape,"brain",reply_to_message_id=editm)
        for i in animation_chars:
            await asyncio.sleep(0.3)
            await bot.edit_message_text(gape,editm,i)

    if word == "تادوج":
        tadog_tag = msg_id
        gap_tadog = grop
        r_s = random.choice(sticker_hap_hap)
        r_t = random.choice(hap_hap)
        await bot.send_message(gap_tadog,r_t,reply_to_message_id=tadog_tag)
        await bot.send_sticker(gap_tadog,r_s)
    if word == "/azl_bot":
        user_king = ch_id
        msg_king = msg_id
        gap_king = grop
        if user_king == "F_2276":
            user85 = m.reply_to_message.from_user.id
            azl_bot.append(user85)
            await bot.send_message(gap_king, "با موفقیت انجام شد!",reply_to_message_id=msg_king)
    if word == "/return":
        user_king2 = ch_id
        msg_king2 = msg_id
        gap_king2 = grop
        if user_king2 == "F_2276":
            user855 = m.reply_to_message.from_user.id
            azl_bot.remove(user855)
            await bot.send_message(gap_king2, "با موفقیت انجام شد!",reply_to_message_id=msg_king2)
    if word == "/anti_spoil on" or word == "اسپویل مود روشن":
        gap_spoil = grop
        admin_id = user_id
        reply_msg = msg_id
        admins1 = await bot.get_chat_members(gap_spoil, filter="administrators")
        for i in admins1:
            if i.user.id == admin_id and i.user.id not in azl_bot:
                if gap_spoil in spoilgap:
                    await bot.send_message(gap_spoil,"آنه",reply_to_message_id=reply_msg)
                else:
                    spoilgap.append(gap_spoil)
                    await bot.send_message(gap_spoil, "اسپویل مود ان شد", reply_to_message_id=reply_msg)
                    await bot.send_sticker(gap_spoil,"CAACAgQAAxkBAALxmGIFdQ1NpOZVLiuM-pzYBFbxGxWKAAKIDgACafIhUMIzeN8QPqayIwQ")
            else:
                pass

    if word == "/anti_spoil off" or word == "اسپویل مود خاموش":
        gap_spoil2 = grop
        reply_msg2 = msg_id
        admin_id2 = user_id
        admins2 = await bot.get_chat_members(gap_spoil2, filter="administrators")
        for i in admins2:
            if i.user.id == admin_id2 and i.user.id not in azl_bot:
                if gap_spoil2 in spoilgap:
                    spoilgap.remove(gap_spoil2)
                    await bot.send_message(gap_spoil2,"اف شد",reply_to_message_id=reply_msg2)
                else:
                    await bot.send_message(gap_spoil2, "اصلا روشن نبود که بخواد خاموش شه", reply_to_message_id=reply_msg2)
            else:
                pass
    if grop in spoilgap:
        reply_spoil = msg_id
        gap_spoil_send = grop
        try:
            for i in m.entities:
                if i.type == "spoiler":
                    spoil_text = str(word)
                    edited_spoil_text = spoil_text.replace("|","")
                    await bot.send_message(gap_spoil_send,edited_spoil_text,reply_to_message_id=reply_spoil)
        except TypeError:
            pass
    if grop not in i_dont_know: 
        adm = await bot.get_chat_members(grop, filter="administrators")
        for i in adm:
            if i.user.id == 2052999223:
                group100 = grop
                i_dont_know.append(group100)
                await bot.send_sticker(group100, "CAACAgQAAxkBAALyCGIHb7IQP9Uyp2c_qDKCseHi_TUsAAJQDQACR5c4UJrAP_6JJ4QIIwQ")
    if word == "ادب":
        global group5
        group5 = grop
        msg_for_reply = msg_id
        admin_id3 = user_id
        admins3 = await bot.get_chat_members(group5, filter="administrators")
        for i in admins3:
            if i.user.id == admin_id3 and i.user.id not in azl_bot:
                if group5 in list_adab_group_id:
                    await bot.send_message(group5,"ادب روشنه دا",reply_to_message_id=msg_for_reply)
                else:
                    list_adab_group_id.append(group5)
                    await bot.send_message(group5, "زین پس هرکس فحش دهد با دستکشم پاک میکنم")
                    await bot.send_sticker(group5,"CAACAgUAAxkBAALtPmH5gdiVKymknZj0DOoqGJfOi6Y9AALuAQAChdHpV-0RMEBGFX7PIwQ")
            else:
                pass
    if word == "ادب خاموش":
        group43 = grop
        msg_for_reply2 = msg_id
        admin_id4 = user_id
        admins4 = await bot.get_chat_members(group43, filter="administrators")
        for i in admins4:
            if i.user.id == admin_id4 and i.user.id not in azl_bot:
                if group43 in list_adab_group_id:
                    list_adab_group_id.remove(grop)
                    await bot.send_message(group43, "زین پس دیگر به ادب حساس نیستم")
                    await bot.send_sticker(group43, "CAACAgUAAxkBAALtImH5Z0ZA8oViTQ9ZQfntpeREWdo9AAJSAgACYC7xV0HEMCL7v_FEIwQ")
            
                else:
                    random_police = random.choice(list_police)
                    await bot.send_message(group43, random_police,reply_to_message_id=msg_for_reply2)
            else:
                pass
    

    if grop in list_adab_group_id:
        maing = grop
            
        if word in fosh:
            msg = msg_id
            user = ch_id
            for_mute = user_id
            if user in user_fosh:
                darage = user_fosh[user]
                if darage == "*":
                    user_fosh[user] = "**"
                    await bot.send_sticker(maing,"CAACAgUAAxkBAALtPmH5gdiVKymknZj0DOoqGJfOi6Y9AALuAQAChdHpV-0RMEBGFX7PIwQ")
                    await bot.send_message(maing,f"دو ستاره شدی برادر یکی از من قوی تر دفعه بعد بهت اخطار میده @{user}")
                    await bot.delete_messages(maing, msg)
                n = 0
                if darage == "**":
                    try:
                        n += 1
                        await bot.restrict_chat_member(maing, for_mute, ChatPermissions(can_send_messages=None),int(time.time() + 120))
                    except:
                        n = -3

                    if n < 0:
                        sticker_cry = random.choice(cry_mute_admin)
                        await bot.send_message(maing, sticker_cry)
                        await bot.send_sticker(maing,"CAACAgQAAxkBAALzCGINFoJcp4FwEzOMh5ryiFG9EqClAAKkCwAChORhUOlwSpp7PIdgIwQ",reply_to_message_id=msg)
                    if n > 0:


                        await bot.send_sticker(maing,"CAACAgUAAxkBAALtQmH5iktBPu5zWw9VQIsBy6r68_VnAAIZAwACnu_oVwpp2bo3TFrkIwQ")
                        await bot.send_message(maing, f"متوجه شدی که سه ستاره شدی گستاخ؟ @{user}")
                        await bot.send_message(maing, f"دو دقیقه به دوزخ میفرستمت @{user}")
                        await bot.delete_messages(maing, msg)
                    else:
                        pass


                if darage == "***":
                    user_fosh[user] = "****"
                    await bot.delete_messages(maing, msg)

                if darage == "****":
                    pass

                if darage == "*****":
                    pass
            else:
                await bot.delete_messages(maing, msg)
                user_fosh[user] = "*"
                randstick = random.choice(sticker_ekhtar_fosh)
                randword = random.choice(dog_fosh)
                await bot.send_sticker(maing,randstick)
                await bot.send_message(maing,randword+" "+"@"+user)
                    
    if word == "/numid":
        gapbemola = grop
        reply_to_user = msg_id
        try:
            user766 = m.reply_to_message.from_user.id
            await bot.send_message(gapbemola,f"numid = {user766}",reply_to_message_id=reply_to_user)
        except:
            await bot.send_message(gapbemola,"ریپلای بزن رو شخص",reply_to_message_id=reply_to_user)

    if "/mute" == word:
        global gap
        global user2
        gap = grop
        tag_adm = msg_id
        admin_id5 = user_id
        admins5 = await bot.get_chat_members(gap, filter="administrators")
        for i in admins5:
            if i.user.id == admin_id5 and i.user.id not in azl_bot:

                try:
                    user2 = m.reply_to_message.from_user.id
                    ask_mute = await bot.ask(gap, "چند ثانیه میوت باشه قربون؟")
                    ask_mute_int = int(ask_mute.text)
                    try:
                        await bot.restrict_chat_member(gap, user2, ChatPermissions(can_send_messages=None),int(time.time() + ask_mute_int))
                        await m.reply(f"قربون مورد نظر به مدت {ask_mute_int / 60}دقیقه  میوت شد")
                        await bot.send_sticker(gap, "CAACAgQAAxkBAALsxGH3HlC7UW2mxjiCn9VtAV_n5lbZAAKoCwACZdpIUzOg02CfO0pPIwQ")
                    except:
                        await bot.send_sticker(gap, "CAACAgQAAxkBAALzCGINFoJcp4FwEzOMh5ryiFG9EqClAAKkCwAChORhUOlwSpp7PIdgIwQ", reply_to_message_id=tag_adm)
                except:
                    id_mute = await bot.ask(gap,"ایدی شخص؟")
                    usernamee = id_mute.text
                    ask_mute = await bot.ask(gap,"چند ثانیه میوت باشه قربون؟")
                    ask_mute_int = int(ask_mute.text)
                    try:
                        await bot.restrict_chat_member(gap, usernamee, ChatPermissions(can_send_messages=None), int(time.time() + ask_mute_int))
                        await m.reply(f"قربون مورد نظر به مدت {ask_mute_int/60}دقیقه  میوت شد")
                        await bot.send_sticker(gap,"CAACAgQAAxkBAALsxGH3HlC7UW2mxjiCn9VtAV_n5lbZAAKoCwACZdpIUzOg02CfO0pPIwQ")
                    except:
                        await bot.send_sticker(gap, "CAACAgQAAxkBAALzCGINFoJcp4FwEzOMh5ryiFG9EqClAAKkCwAChORhUOlwSpp7PIdgIwQ", reply_to_message_id=tag_adm)
            else:
                pass

    if "/unmute" in word:
        gap2 = grop
        admin_id6 = user_id
        admins6 = await bot.get_chat_members(gap2, filter="administrators")
        for i in admins6:
            if i.user.id == admin_id6 and i.user.id not in azl_bot:

                try:
                    user3 = m.reply_to_message.from_user.username
                    await bot.restrict_chat_member(gap2, user3,ChatPermissions(can_send_messages=True))
                    await m.reply("فرد مورد نظر با دستکشم ان میوت شد")
                    await bot.send_sticker(gap2,"CAACAgQAAxkBAALsxGH3HlC7UW2mxjiCn9VtAV_n5lbZAAKoCwACZdpIUzOg02CfO0pPIwQ")
                except:
                    id_ba = await bot.ask(gap2,"ایدی شخص؟")
                    id_ba_reply = id_ba.text
                    await bot.restrict_chat_member(gap2,id_ba_reply , ChatPermissions(can_send_messages=True))
                    await m.reply("فرد مورد نظر با دستکشم ان میوت شد")
                    await bot.send_sticker(gap2,"CAACAgQAAxkBAALsxGH3HlC7UW2mxjiCn9VtAV_n5lbZAAKoCwACZdpIUzOg02CfO0pPIwQ")
            else:
                pass

    if word == "/del_gap":
        sayr = random.choice(say)
        global group
        group = grop
        admin_id7 = user_id
        admins7 = await bot.get_chat_members(group, filter="administrators")
        for i in admins7:
            if i.user.id == admin_id7:
                rstick = random.choice(stickers)
                await bot.send_sticker(group,rstick)
                await m.reply(f"عدد رو وارد کن {sayr}")
            else:
                pass
    if  word == "/del_me":
        group2 = grop
        userid = ch_id
        await bot.send_sticker(group2,"CAACAgQAAxkBAALyEGIHcLY3hZu4FX-vy79iF9nsOFkGAAK4CgACEQs4UDcWnrLOkf_5IwQs")
        time.sleep(1)
        mid = msg_id+1
        try:
            await bot.delete_messages(group2, mid)
            await bot.delete_user_history(group2, userid)
            await bot.send_message(group2, f"تمام پیامات توسط دستکش تادوج پاک شد ( @{userid}  )")
        except:
            await bot.send_message(group2,"دستکشم کار نکرد چون ادمین نیستم")
            await bot.send_sticker(group2, "CAACAgQAAxkBAALzCGINFoJcp4FwEzOMh5ryiFG9EqClAAKkCwAChORhUOlwSpp7PIdgIwQ")
            
    
    
    javab = m.reply_to_message.text
    if javab == "عدد رو وارد کن کیومرث" or javab == "عدد رو وارد کن قربون":
        admin_id8 = user_id
        admins8 = await bot.get_chat_members(group, filter="administrators")
        for i in admins8:
            if i.user.id == admin_id8 and i.user.id not in azl_bot:
                try:
                    ada = str(word)
                    adad = int(ada)


                    await bot.send_sticker(group,"CAACAgQAAxkBAALyEGIHcLY3hZu4FX-vy79iF9nsOFkGAAK4CgACEQs4UDcWnrLOkf_5IwQs")
                    time.sleep(1)

                    n = adad
                    async for i in bot.search_messages(group, limit=adad):
                        n -= 1
                        try:
                            await bot.delete_messages(group, i.message_id)

                            if n == 1:
                                await bot.send_message(group, f"تعداد {adad} پیام با دستکش خوشگلم پاک شد")
                                await bot.send_sticker(group,"CAACAgQAAxkBAALsxGH3HlC7UW2mxjiCn9VtAV_n5lbZAAKoCwACZdpIUzOg02CfO0pPIwQ")
                        except:
                            await bot.send_message(group, "دستکشم کار نکرد چون ادمین نیستم")
                            await bot.send_sticker(group, "CAACAgQAAxkBAALzCGINFoJcp4FwEzOMh5ryiFG9EqClAAKkCwAChORhUOlwSpp7PIdgIwQ")
                except:
                    await bot.send_sticker(group, "CAACAgQAAxkBAALswGH3HE_DIV5xor2ktq5xY-4r8_kCAAJBCwACr6lAU6mz1uo56lloIwQ")
                    await bot.send_message(group,"این که عدد نیست کیومرث")
            else:
                pass

bot.run()