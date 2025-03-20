import time

def start_game():
    print("在遙遠的王國裡，有一位名叫艾莉雅的公主。她不喜歡金碧輝煌的宮殿，也不喜歡宴會上那些虛偽的笑容。她嚮往未知的冒險，想要探索世界的神秘之處。有一天，她來到了一座古老的森林——黑森林。")
    print("這座森林被傳說籠罩，據說裡面住著會說話的野獸、會變幻形體的湖泊，還有迷失在時光中的幽靈。但艾莉雅並不害怕，她輕輕掀起斗篷，邁步走了進去。走了不久，霧氣漸漸濃厚，她發現前方有三條小徑")
    print("她看到前方有兩條路：左邊和右邊。")
    choose_path()

def choose_path():
    choice = input("你要選擇哪條路？（左/右）")
    if choice == "左":
        left_path()
    elif choice == "右":
        right_path()
    else:
        print("請輸入「左」或「右」。")
        choose_path()

def left_path():
    print("她沿著左邊的路走，跟隨銀色的光點 —— 一串微光在前方閃爍，像是在引領她前進。")
    print("她發現一個破舊的小屋，裡面傳來微弱的光。")
    choice = input("要進去小屋嗎？（是/否）")
    if choice == "是":
        enter_house()
    elif choice == "否":
        print("她決定繼續往前走，走向低語的樹林 —— 風中傳來細細的低語，像是樹木在交談，她想聽清楚。")
        time.sleep(2)
        print("遊戲結束，結局 1：森林的賢者告訴她，她的命運是要拯救這片森林。")

    else:
        print("請輸入「是」或「否」。")
        left_path()

def right_path():
    print("你沿著右邊的路走，遇到一條湍急的河流。")
    print("艾莉雅沿著河走，發現水面倒映的不是自己，而是一個穿著破舊長袍的女人。女人的影像張口說話：「妳想要知道自己的命運嗎？」語氣帶著一絲哀傷。")
    choice = input("妳想要知道自己的命運嗎？（是/否）")
    if choice == "是":
        cross_bridge()
    elif choice == "否":
        print("她相信命運掌握在自己手中，不需要預言。")
        time.sleep(2)
        print("遊戲結束，結局 2：艾莉雅在黑森林中迷路，最後被一隻會說話的野獸吃掉了")
    else:
        print("請輸入「是」或「否」。")
        right_path()

def enter_house():
    print("艾莉雅跟著光點走，發現自己來到了一座廢棄的神殿。神殿的大門上刻著一行古老的文字，而光點停在門口，不再前進。艾莉雅感覺到一股神秘的力量在吸引她靠近。")
    time.sleep(2)
    print("她推開大門，看到一位老巫婆坐在石凳上。")
    time.sleep(1)
    print("老巫婆微笑著問她：「我有一個問題，你知道答案嗎？」")
    answer = input("你的答案是什麼？")
    if answer == "泡泡" : #可以有很多種答案
       print ("老巫婆點點頭，並給你一把鑰匙")
       time.sleep(1)
       print ("你打開了寶箱，裡面裝滿了金幣，你贏得了勝利！")
    else :
      print ("老巫婆搖搖頭，並把你變成一隻青蛙")
      time.sleep(2)
      print("遊戲結束，你失敗了。")

def cross_bridge():
    print("女人告訴艾莉雅，她的命運是要找到一座橋，橋的另一端是她的未來。")
    print("艾莉雅繼續走，發現了一座橋。")
    choice = input("你要過橋嗎？（是/否）")
    if choice == "是":
        print("她踏上橋，走到橋的另一端。")
        time.sleep(2)
        print("遊戲結束，結局 3：她找到了一座神秘的城堡，城堡裡住著一位神秘的王子。")
    elif choice == "否":
        print("她決定不過橋，轉身離開黑森林。")
        time.sleep(2)
        print("遊戲結束，結局 4：她回到了王國，過著平凡的生活。")
    else:
        print("請輸入「是」或「否」。")
        cross_bridge()
  

start_game()