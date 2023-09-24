

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
            print("\nYour choice regarding Nepal's direction will impact the nation's path forward, whether it's building a stable internal foundation, expanding its influence externally, or preserving its cultural identity.")

#exe
