# restfulAPI
practice of restful API with MySQL on RDS and app on Heroku

---

# 說明

前言
我自己寫了幾個範例的API讓大家在寫作時可以呼叫，模擬上線後呼叫其他API的行為。因此JSON傳遞的內容也都是遵照規範，所以可以放心使用。

另外，也可以檢查自己完成api有沒有符合輸出的規範，照理說寫好的api應該要可以被我呼叫喔～

大家加油，辛苦大家了！！

---

## API 1
網址: https://simsysapi.herokuapp.com/sim/kernel <br />
方法: GET<br />
功能: 模擬推薦商品服務提供的API<br />
輸入: <br />
{<br />
"json":{<br />
"userId": 使用者ID,<br />
"cur_state": 使用者目前狀態,<br />
"subject": 送禮對象,<br />
"interested_things": 興趣類別,<br />
"conds": 有興趣的標籤們,<br />
"next_tag": 下一個詢問的標籤,<br />
"product_cnt": 候選禮物數<br />
},<br />
"outside":{<br />
"action": 使用者傳來的訊息類別,"msg": 使用者輸入的文字訊息<br />
}<br />
}<br />
輸出:<br />
{<br />
    "json": {<br />
        "conds": ["出國", "日本" ],<br />
        "cur_state": "first_question",<br />
        "interested_things": "音樂",<br />
        "next_tag": "飛機",<br />
        "product_cnt": 31,<br />
        "subject": "母親",<br />
        "userId": "2020081000011"<br />
    		},<br />
    "reply": {<br />
        "close": false<br />
  		}<br />
}<br />
 <br />
 <br />
 
## API 2
網址: https://simsysapi.herokuapp.com/sim/thxword<br />
方法: GET<br />
功能: 模擬 文本詞生成器提供的API<br />
輸入: <br />
	input: { "subject": "NAME0", <br />
		"conds": ["TAG1", "TAG2", "TAG3", ...]<br />
		}<br />
輸出:<br />
output: {<br />
"thx words": "感謝詞（可以用在卡片上）\n===\n親愛的 NAME0\n\n幸福的生活中少不了你的陪伴。\n\n我知道你喜歡tag1、tag2、tag3，所以特地挑選了這個禮物，希望你會喜歡。"}<br />
<br />
<br />

## API 3
網址: https://simsysapi.herokuapp.com/sim/productA<br />
方法: GET<br />
功能: 模擬 產品服務提供的API，提供一組標籤，回傳下一個標籤、候選商品數量<br />
輸入: <br />
	input: { "conds": ["TAG1", "TAG2", "TAG3", ...] }<br />
輸出:<br />
output: {“next_tag”: “NEWTAG”, <br />
 “product_cnt”: 正整數<br />
}<br />
輸出範例:<br />
{<br />
    "next_tag": "法律",<br />
    "product_cnt": 5<br />
}<br />
<br />
<br />

## API 4
網址: https://simsysapi.herokuapp.com/sim/productB<br />
方法: GET<br />
功能: 模擬 產品服務提供的API<br />
輸入: <br />
	input: { "conds": ["TAG1", "TAG2", "TAG3", ...] }<br />
輸出:<br />
output: {“products”: [ {“name”: “PRODUCT0_NAME”, “url”: “PRODUCT0_URL”},<br />
          {“name”: “PRODUCT1_NAME”, “url”: “PRODUCT1_URL”},<br />
… ] }<br />
輸出範例:<br />
{<br />
    "products": [<br />
        {<br />
            "name": "NOKIA 2720 Flip大按鍵大字體4G雙卡經典摺疊手機",<br />
            "url": "https://tw.buy.yahoo.com/gdsale/NOKIA-2720-Flip%E5%A4%A7%E6%8C%89%E9%8D%B5%E5%A4%A7%E5%AD%97%E9%AB%944G%E9%9B%99%E5%8D%A1-8848561.html"<br />
        },<br />
        {<br />
            "name": "HP 超品 15s-du1048TU 15吋筆電(N5030/4G/256G SSD/Win10/星沙金)",<br />
            "url": "https://tw.buy.yahoo.com/gdsale/HP-%E8%B6%85%E5%93%81-15s-du1048TU-15%E5%90%8B%E7%AD%86%E9%9B%BB-N5030-4G-256G-SSD-Win10-%E6%98%9F-9045909.html"<br />
        },<br />
        {<br />
            "name": "HERLS 全真皮英倫雅痞綁帶牛津鞋-棕色",<br />
            "url": "https://tw.buy.yahoo.com/gdsale/HERLS-%E5%85%A8%E7%9C%9F%E7%9A%AE%E8%8B%B1%E5%80%AB%E9%9B%85%E7%97%9E%E7%B6%81%E5%B8%B6%E7%89%9B%E6%B4%A5%E9%9E%8B-%E6%A3%95%E8%89%B2-7080873.html"<br />
        },<br />
        {<br />
            "name": "橘子工坊 天然濃縮洗衣精補包組 制菌力99.99%1500ml+200ml x6包組",<br />
            "url": "https://tw.buy.yahoo.com/gdsale/%E6%A9%98%E5%AD%90%E5%B7%A5%E5%9D%8A-%E5%A4%A9%E7%84%B6%E6%BF%83%E7%B8%AE%E6%B4%97%E8%A1%A3%E7%B2%BE%E8%A3%9C%E5%85%85%E5%8C%851500ml-200-7697309.html"<br />
        },<br />
        {<br />
            "name": "一匙靈 ATTACK 抗菌EX科技潔淨洗衣精 (瓶裝2.4kg)",<br />
            "url": "https://tw.buy.yahoo.com/gdsale/%E4%B8%80%E5%8C%99%E9%9D%88-ATTACK-%E6%8A%97%E8%8F%8CEX%E7%A7%91%E6%8A%80%E6%BD%94%E6%B7%A8%E6%B4%97%E8%A1%A3%E7%B2%BE-%E7%93%B6%E8%A3%9D-7743879.html"<br />
        },<br />
        {<br />
            "name": "BuyJM蓆面五段三折躺椅/萬年床-免組",<br />
            "url": "https://tw.buy.yahoo.com/gdsale/BuyJM%E8%93%86%E9%9D%A2%E4%BA%94%E6%AE%B5%E4%B8%89%E6%8A%98%E8%BA%BA%E6%A4%85-%E8%90%AC%E5%B9%B4%E5%BA%8A-%E5%85%8D%E7%B5%84-6626010.html"<br />
        }<br />
    ]<br />
}<br />
<br />
<br />
