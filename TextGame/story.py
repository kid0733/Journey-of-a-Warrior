class story:
    def __init__(self) -> None:
        self.ph='placeholder'
        self.isABitch=0
        self.isGangsta=0
    def showScore(self):
        print(f"Your 'Is a Bitch Score is:' {self.isABitch}")
        print(f"Your 'Is Gangsta Score is:' {self.isGangsta}")
    def showCredits(self):
        print("\n\nThankyou for playing the Journey of a Warrior. Have a nice day :)\nDirector: Siddhant\nWriter:ChatGPT\nCoder:Siddhant");
    def scene_1(self):
        while True:
            #Intro
            print("\n\nScene 1: The Messenger's Invitation\n\n")
            print("\n\nYou stand amidst the lush greenery of your home, a small kingdom nestled in the picturesque hills of Nepal.\n The tranquility of the landscape is interrupted by the distant sound of hooves approaching. Your curiosity piqued, you gaze down the winding path that leads to your village.\n")
            print("A cloud of dust approaches, and soon, a lone rider on horseback comes into view. It's a messenger, wearing the colors of the Gorkha kingdom. He rides with an air of urgency, and his steed is lathered in sweat.\n\n")
            print("The messenger reins in his horse before you and dismounts. He bows respectfully and hands you a sealed scroll adorned with the royal seal of King Prithvi Narayan Shah. With a solemn tone, he delivers a message:\n\nHail, brave warrior of Nepal! His Majesty, King Prithvi Narayan Shah, extends his invitation to you. The unity of our land beckons, and your valor is needed in Gorkha. Join the ranks of the Gorkha army, and together, we shall forge a united Nepal.\n\n")
            print("The messenger awaits your response, his eyes filled with anticipation. The choice is yours: Will you accept the invitation and embark on a journey that could change the course of history?")
            #Choice to accept invitation to army
            user_choice=input("\nPlease type the letter:\nA: Accept the Invitation: You decide to accept the invitation and set forth on a journey to Gorkha.\nB: Decline the Invitation: You decline the invitation, choosing to remain in your homeland.\n\nYour decision here will shape the course of your adventure. Choose wisely.\n")
            if user_choice.lower()=='b':
                self.showCredits()
                self.isABitch+=1
                self.isGangsta-=1
                self.showScore()
                break;
            elif user_choice.lower()=='a':
                print("And so our hero sets on [insert gender]'s journey, to get their ass whooped by a bunch of random people.\n")
                self.isGangsta+=1
                break;
            else:
                print('That was an invalid input')
                self.isABitch+=1;
    
    def scene_2(self):
        while True:
            print('\n\nScene 2: The Journey to Gorkha\n\n')
            print("\nHaving accepted the invitation, you make preparations for the long journey to Gorkha, the heart of Nepal's unification efforts. The road ahead is fraught with challenges, and you know that every step will test your mettle.\n\nAs you bid farewell to your family and friends, the weight of your decision hangs heavy. You embark on the winding path that leads down the hills and into the unknown.")
            user_choice=input("\nPlease type the letter:\nA: Brace for Adventure: You embrace the adventure and face the challenges ahead with determination. This choice signifies your resolve to overcome obstacles.\nB: Doubts Creep In: Doubts creep into your mind as you journey further from home. You wonder if you've made the right choice.\n\n")
            if user_choice.lower()=='b':
                print("\n\nSo, our great hero ran home, away from his true destiny, like the bitch [insert gender here]'s was. (idk i dont want to get cancelled over a text based game)\n\n")
                self.isABitch+=1
                self.isGangsta-=1
                self.showScore()
                break;
            elif user_choice.lower()=='a':
                print('\n\nThe path ahead is filled with uncertainty, but your determination fuels your progress. Each step takes you closer to Gorkha, where your fate will be decided.\n\n')
                self.isGangsta+=1
                break;
            else:
                print('That was an invalid input')
                self.isABitch+=1;
    
    def scene_3(self):
        while True:
            print("\n\nScene 3: Arrival in Gorkha")
            print("\n\n\nAfter days of travel, you finally arrive in Gorkha, the heart of King Prithvi Narayan Shah's realm. The towering hillsides, the bustling markets, and the magnificent palace atop the hill all greet you as you enter the city.\nHowever, the warm welcome you'd hoped for isn't immediate. You're met with skepticism from the locals and the warriors who have long served King Prithvi Narayan Shah. They eye you cautiously, questioning your intentions and abilities.\nIt's clear that earning their trust won't be easy, but it's essential if you are to fulfill your destiny in Gorkha.")
            user_choice=input("\nPlease type the letter:\nA: Approach Diplomatically: You decide to use diplomacy to win over the locals. You seek out the local leaders to engage in discussions and form alliances.\n\nB: Espionage and Reconnaissance: You opt for a more secretive approach. You gather information about the power dynamics in Gorkha and try to uncover any potential threats.\n\nC:Challenge in Combat: You believe that actions speak louder than words. You challenge a respected warrior to a duel, hoping to prove your worth through combat.\n\nYour choice here will shape how you begin to establish yourself in Gorkha and how others perceive you.")
            if user_choice.lower()=='a':
                print("\nYou decide to approach the situation diplomatically, recognizing the importance of building alliances and trust. You seek out the local leaders of Gorkha, engaging in conversations and negotiations.\n")
                self.isGangsta+=3#gangsta moves in scilence
                break;
            elif user_choice.lower()=='b':
                print("\nYou choose to take a secretive approach, believing that knowledge is power. You discreetly gather information about the power dynamics in Gorkha and keep an eye on potential threats.\n")
                self.isABitch+=2
                break;
            elif user_choice.lower()=='c':
                print("\nYou decide to prove your worth through combat, believing that actions speak louder than words. You challenge a respected warrior in Gorkha to a duel, a daring move.\n")
                self.isGangsta+=2
                self.isABitch+=1
                break;
            else:
                print('Thats not a valid reply')
            print("\nyou've taken your first steps to establish yourself in Gorkha. The path ahead will be shaped by your interactions and alliances in the city. Your decisions will determine how you navigate the challenges that lie ahead in your historical Nepali adventure.")

    def scene_4(self):
        while True:
            print("\n\nScene 4: The Council of Unity")
            print("\n\n\nAs time passes and you establish yourself in Gorkha, the kingdom faces internal and external challenges. The council convened by King Prithvi Narayan Shah seeks to address these challenges and forge a united Nepal.")
            user_choice=input("\nPlease type the letter:\nA: Active Participant: You actively participate in the council, offering your insights and suggestions. This choice reflects your dedication to the cause of unity.\nB: Observer: You choose to observe the council's proceedings without actively participating. This decision allows you to assess the political landscape before fully committing.\nC: Skeptical Dissenter: You voice your skepticism about the council's objectives, questioning whether unity is truly achievable. This choice may set you on a different path.")
            if user_choice.lower()=='a':
                print("\nYou choose to actively participate in the council, demonstrating your dedication to the cause of unity. Your insights and suggestions are well-received by some council members, and your voice carries weight.\n")
                self.isABitch+=3#I know you be a curropt politician if you chose this
            elif user_choice.lower()=='b':
                print("\nOpting to observe the council proceedings allows you to assess the political landscape before fully committing. You gain valuable insights into the various factions and their agendas.\n")
                self.isGangsta+=3#gangsta moves in scilence
                break;
            elif user_choice.lower()=='c':
                print("\nYou choose to voice your skepticism about the council's objectives, questioning whether unity is truly achievable. This decision sets you on a different path, challenging the status quo.\n")
                self.isABitch+=2
                self.isGangsta+=1#giving varys
                break;
            else:
                print('Thats not a valid reply')
            print("\nYour choice in this pivotal scene will significantly impact your role in shaping Nepal's destiny and the challenges you'll face as the game progresses.")
    
    def scene_5(self):
        while True:
            print("\n\nScene 5: A Diplomatic Mission")
            print("\n\n\nThe council's efforts to unite Nepal have faced setbacks, and King Prithvi Narayan Shah decides to send emissaries to neighboring kingdoms to seek alliances and support. You are chosen as one of the emissaries for this crucial diplomatic mission.")
            user_choice=input("\nPlease type the letter:\nA: Forge Alliances: You actively seek to forge alliances with neighboring kingdoms, emphasizing the benefits of unity for all.\n\nB:Gather Information: You prioritize gathering information during the diplomatic mission, hoping to uncover hidden agendas and threats.\n\nC:Question the Mission: You question the effectiveness of diplomatic efforts, wondering if there are more direct ways to achieve unity.")
            if user_choice.lower()=='a':
                print("\nYou choose to actively seek to forge alliances with neighboring kingdoms, emphasizing the benefits of unity for all. Your diplomatic skills and persuasive arguments are put to good use.\n")
                self.isGangsta+=2
                self.isABitch+=1
                break;
            elif user_choice.lower()=='b':
                print("\nPrioritizing the gathering of information during the diplomatic mission, you hope to uncover hidden agendas and threats. Your keen observation skills and discretion serve you well.\n")
                
                self.isGangsta+=3#gangsta moves in scilence
                break;
            elif user_choice.lower()=='c':
                print("\nYou question the effectiveness of diplomatic efforts, wondering if there are more direct ways to achieve unity. Your skepticism leads you to consider alternative paths.\n")
                self.isABitch+=4
                break;
            else:
                print('Thats not a valid reply')
            print("\nyou've taken your first steps to establish yourself in Gorkha. The path ahead will be shaped by your interactions and alliances in the city. Your decisions will determine how you navigate the challenges that lie ahead in your historical Nepali adventure.")

    def scene_6(self):
        while True:
            print("\n\nScene 6: The Battle of Kirtipur")
            print("\n\n\nTensions rise as Nepal's unification efforts continue. The kingdom of Kirtipur stands as a formidable obstacle to unity. King Prithvi Narayan Shah decides to lead an army to confront this challenge head-on.")
            user_choice=input("\nPlease type the letter:\nA: Lead the Charge: You join the king's army and play an active role in the battle against Kirtipur. Your bravery inspires the troops.\n\nB: Strategic Advisor: You take on the role of a strategic advisor, helping plan the battle's tactics and logistics.\n\nC: Observer: You choose to observe the battle from a safe distance, focusing on assessing the situation.\n\nYour choice in this pivotal battle scene will shape the outcome of the Battle of Kirtipur and your character's role in the ongoing unification efforts.")
            if user_choice.lower()=='a':
                print("\nYou choose to join the king's army and play an active role in the battle against Kirtipur. Your bravery on the battlefield inspires the troops, and you become a symbol of courage.\n")
                self.isGangsta+=5
                self.isABitch-=1
                break;
            elif user_choice.lower()=='b':
                print("\nOpting to become a strategic advisor, you focus on planning the battle's tactics and logistics. Your expertise contributes to a well-thought-out battle strategy.\n")
                
                self.isGangsta+=3#gangsta moves in scilence
                self.isABitch+=1
                break;
            elif user_choice.lower()=='c':
                print("\nYou choose to observe the battle from a safe distance like the bitch you have chosen to be, concentrating on assessing the situation without direct involvement.\n")
                self.isABitch+=6
                break;
            else:
                print('Thats not a valid reply')
            print("\nyou've taken your first steps to establish yourself in Gorkha. The path ahead will be shaped by your interactions and alliances in the city. Your decisions will determine how you navigate the challenges that lie ahead in your historical Nepali adventure.")

    def scene_7(self):
        while True:
            print("\n\nScene 7: Aftermath and Consequences")
            print("\n\n\nThe Battle of Kirtipur is over, and the outcome will significantly affect the future of Nepal. This scene explores the immediate aftermath and its consequences.")
            user_choice=input("\nPlease type the letter:\nA: Rebuild Kirtipur: You advocate for a policy of rebuilding and reconciliation with the people of Kirtipur, fostering unity within Nepal.\n\nB: Consolidate Power: You suggest a strategy to consolidate power swiftly, solidifying control over recently conquered territories.\n\nC: Seek Diplomacy: You propose opening diplomatic negotiations with the remnants of Kirtipur, aiming for a peaceful resolution.")
            if user_choice.lower()=='a':
                print("\nYou advocate for a policy of rebuilding and reconciliation with the people of Kirtipur, emphasizing unity within Nepal.\n")
                self.isGangsta+=3
                break;
            elif user_choice.lower()=='b':
                print("\nOpting to become a strategic advisor, you focus on planning the battle's tactics and logistics. Your expertise contributes to a well-thought-out battle strategy.\n")
                
                self.isGangsta+=3#gangsta moves in scilence
                self.isABitch+=1
                break;
            elif user_choice.lower()=='c':
                print("\nYou choose to observe the battle from a safe distance like the bitch you have chosen to be, concentrating on assessing the situation without direct involvement.\n")
                self.isABitch+=6
                break;
            else:
                print('Thats not a valid reply')
            print("\nYour choice in this crucial aftermath scene will impact the stability of the newly unified Nepal and set the tone for future governance and diplomacy.")

    def scene_8(self):
        while True:
            print("\n\nScene 8: The Coronation")
            print("\n\n\nWith the unification of Nepal progressing, it is time to consider the coronation of King Prithvi Narayan Shah as the ruler of the unified nation.")
            user_choice=input("\nPlease type the letter:\nA: Grand Celebration: You advocate for a grand and public coronation ceremony to symbolize the unity of Nepal. This choice emphasizes spectacle and unity.\n\nB: Low-Key Ceremony: You suggest a low-key, private coronation to avoid drawing attention and potential threats from neighboring kingdoms. This choice prioritizes security.\n\nC: Ceremony Abroad: You propose holding the coronation in a neutral foreign land to gain international recognition and support. This choice emphasizes diplomacy.")
            if user_choice.lower()=='a':
                print("\nYou advocate for a grand and public coronation ceremony to symbolize the unity of Nepal. This choice emphasizes spectacle and unity.\n")
                self.isGangsta-=3#Bitch be humble
                break;
            elif user_choice.lower()=='b':
                print("\nYou suggest a low-key, private coronation to avoid drawing attention and potential threats from neighboring kingdoms. This choice prioritizes security.\n")
                
                self.isGangsta+=3#gangsta moves in scilence
                self.isABitch+=1
                break;
            elif user_choice.lower()=='c':
                print("\nYou propose holding the coronation in a neutral foreign land to gain international recognition and support. This choice emphasizes diplomacy.\n")
                self.isABitch+=1
                self.isGangsta+=1
                break;
            else:
                print('Thats not a valid reply')
            print("\nYour choice regarding the coronation ceremony will impact how Nepal is perceived on the international stage and may have implications for its diplomatic relations.")

    def scene_9(self):
        while True:
            print("\n\nScene 9: Diplomatic Relations")
            print("\n\n\nNepal's unification efforts have garnered attention from neighboring kingdoms and foreign powers. It's time to consider how Nepal will navigate its diplomatic relations.")
            user_choice=input("\nPlease type the letter:\nA: Open for Alliances: You advocate for seeking alliances with neighboring kingdoms to strengthen Nepal's position and security.\n\nB: Neutrality: You propose a policy of neutrality, avoiding entanglements in the conflicts of neighboring kingdoms.\n\nC: Assertive Diplomacy: You suggest assertive diplomacy to assert Nepal's sovereignty and negotiate favorable terms with other powers.")
            if user_choice.lower()=='a':
                print("\nYou advocate for seeking alliances with neighboring kingdoms to strengthen Nepal's position and security.\n")
                self.isGangsta+=2
                self.isABitch+=1
                break;
            elif user_choice.lower()=='b':
                print("\nYou propose a policy of neutrality, avoiding entanglements in the conflicts of neighboring kingdoms.\n")
                
                self.isGangsta+=1
                self.isABitch+=3
                break;
            elif user_choice.lower()=='c':
                print("\nYou suggest assertive diplomacy to assert Nepal's sovereignty and negotiate favorable terms with other powers.\n")
                self.isABitch-=1
                self.isGangsta+=3
                break;
            else:
                print('Thats not a valid reply')
            print("\nYour choice regarding Nepal's diplomatic approach will influence the nation's standing in the region and its interactions with neighboring kingdoms and foreign powers.")

    def scene_10(self):
        while True:
            print("\n\nScene 10: A New Challenge")
            print("\n\n\nAs Nepal consolidates its territory and navigates diplomatic relations, a new challenge emerges on the horizon.")
            user_choice=input("\nPlease type the letter:\nA: Internal Stability: You prioritize internal stability, focusing on governance and addressing issues within Nepal's borders.\n\nB: External Expansion: You advocate for expansion beyond Nepal's current borders, seeking to assert dominance in the region.\n\nC: Cultural Preservation: You propose a policy of cultural preservation, safeguarding Nepal's rich heritage and traditions.")
            if user_choice.lower()=='a':
                print("\nYou prioritize internal stability, focusing on governance and addressing issues within Nepal's borders.\n")
                self.isGangsta+=2
                self.isABitch+=1
                break;
            elif user_choice.lower()=='b':
                print("\nYou advocate for expansion beyond Nepal's current borders, seeking to assert dominance in the region.\n")
                
                self.isGangsta+=4
                self.isABitch+=0
                break;
            elif user_choice.lower()=='c':
                print("\nYou propose a policy of cultural preservation, safeguarding Nepal's rich heritage and traditions.\n")
                self.isABitch-=1
                self.isGangsta+=5
                break;
            else:
                print('Thats not a valid reply')
            print("\nYour choice regarding Nepal's direction will impact the nation's path forward, whether it's building a stable internal foundation, expanding its influence externally, or preserving its cultural identity.")
    def scene_11(self):
        while True:
            print("\n\nScene 11: The Path Forward")
            print("\n\n\nNepal has faced critical decisions and challenges on its journey to becoming a unified nation. Now, it's time to decide on the path forward.")
            user_choice = input("\nPlease type the letter:\n"
                                "A: Modernization: You advocate for modernization, embracing technological and societal advancements to propel Nepal into the future.\n"
                                "B: Tradition and Heritage: You prioritize the preservation of Nepal's rich cultural traditions and heritage, valuing continuity over rapid change.\n"
                                "C: Balanced Approach: You propose a balanced approach that combines modernization with the preservation of cultural values.")
            if user_choice.lower() == 'a':
                print("\nYou advocate for modernization, embracing technological and societal advancements to propel Nepal into the future.")
                self.isGangsta+=1
                self.isABitch+=2
                break
            elif user_choice.lower() == 'b':
                print("\nYou prioritize the preservation of Nepal's rich cultural traditions and heritage, valuing continuity over rapid change.")
                self.isGangsta+=1
                self.isABitch+=1
                break
            elif user_choice.lower() == 'c':
                print("\nYou propose a balanced approach that combines modernization with the preservation of cultural values.")
                self.isGangsta+=3
                self.isABitch+=1
                break
            else:
                print('Thats not a valid reply')
            print("\nYour choice regarding Nepal's path forward will define its trajectory, balancing modernization and cultural preservation.")

    def scene_12(self):
        while True:
            print("\n\nScene 12: The Legacy of Nepal")
            print("\n\n\nAs Nepal progresses along the chosen path, it's time to reflect on the legacy that will be left for future generations.")
            user_choice = input("\nPlease type the letter:\n"
                                "A: Legacy of Prosperity: You aim to leave a legacy of economic prosperity, with Nepal becoming a thriving and influential nation.\n"
                                "B: Legacy of Culture: You prioritize leaving a legacy of rich cultural heritage, ensuring that Nepal's traditions continue to thrive.\n"
                                "C: Legacy of Balance: You seek to leave a legacy of balance, where Nepal stands as a modernized nation without losing its cultural identity.")
            if user_choice.lower() == 'a':
                print("\nYou aim to leave a legacy of economic prosperity, with Nepal becoming a thriving and influential nation.")
                self.isGangsta+=5
                self.isABitch+=1
                break;
                
            elif user_choice.lower() == 'b':
                print("\nYou prioritize leaving a legacy of rich cultural heritage, ensuring that Nepal's traditions continue to thrive.")
                self.isGangsta+=3
                self.isABitch+=1
                
                break
            elif user_choice.lower() == 'c':
                print("\nYou seek to leave a legacy of balance, where Nepal stands as a modernized nation without losing its cultural identity.")
                self.isGangsta+=5
                self.isABitch+=0
                break
            else:
                print('Thats not a valid reply')
            print("\nYour choice regarding Nepal's legacy will shape how the nation is remembered in history.")

    
    #run
    def run(self):
        self.scene_1()
        self.scene_2()
        self.scene_3()
        self.scene_4()
        self.scene_5()
        self.scene_6()
        self.scene_7()
        self.scene_8()
        self.scene_9()
        self.scene_10()
        self.scene_11()
        self.scene_12()
        self.showScore()
        print("\n\nThankyou for playing the Journey of a Warrior. Have a nice day :)\nDirector: Siddhant\nWriter:ChatGPT\nCoder:Siddhant");
if __name__=="__main__":
    play=story()
    play.run()


