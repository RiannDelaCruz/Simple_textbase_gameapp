def main_text():
	return {
	-1:"""Instructions:\n\nThis a decision-based game that has multiple endings determined by your choices. Read the story and determine your fate by clicking on the corresponding buttons. Think simple and remember to enjoy the game.
	""",
	0:"""
	It’s 3 in the morning when you decide to go home. Wearing a pair of blue jeans, a white tainted shirt and your old rubber shoes, you pass by a grocery store and decide to buy something you can bring home. You enter the store and approach the food aisle. You get two loaves of bread, a jar of jam and something to drink. You approach the counter to pay for your items and while paying, you see someone familiar entering a narrow alleyway near the opposite side of the street. You exit the shop with your groceries in hand, and decide to follow that person. The alleyway was slightly dark. The only source of light is an old street light at the end of the ally. You get closer and closer to the person but by the time you realize it, he was nowhere to be seen. You decide to go back. However, as you turn your head, you suddenly felt dizzy and lose consciousness.
	""",
	1:"""
	You can smell an unpleasant odor that makes you want to throw up. You feel so numb and your body aches all over. You try to open your eyes but you didn't expect the sight before you. There is blood scattered everywhere and bodies lying on the ground. Your whole body is shivering in fear not knowing if they are dead or not. As you regain your composure, your instinct tells you that you need to get out of there right away, so you look for an exit. As you search the place, you have observed that it is somewhat familiar. Without the blood stains everywhere, it looks like a place you are used to seeing everyday. Your heart beats faster not wanting to believe what you are currently thinking. "No!, it’s impossible! How can I be here?!"...You are trying to recall everything that happened but you can't.
	""",
	2:"""
	You took the courage to get up and look around to search for some clues that might help you remember. You decide to enter a room. You see that there is a bathroom inside so you go in but take a deep breath first. You take a glance at the mirror and see yourself covered in blood. "I need to clean myself first", you exit the bathroom and see a cabinet at a corner near a broken window. You search for a change of clothes to replace your blood-stained attire. You go back inside the bathroom and locked the door thinking that maybe, the killer is just nearby watching and getting ready to kill you! But who is the person behind all of this?...why am I here?...why am I the only person alive?...Questions started to linger in your mind as the water started to splash from your face to every part of your body washing out the blood stains on your skin. 
	""",
	3:"""
	You are afraid to go back. After cleaning yourself, you just wanted to stay inside the bathroom out of fear. However, a part of yourself really wanted to know what happened. You built up some courage and decided to take the risk. You decide to go back to that horrible place, hoping that everything was just a dream but what you are seeing is still the same. Your eyes scan around the room trying to understand what had really happened here. You suddenly remembered how different this place is compared to usual. Everything is messed up. The peach white wall is now covered with red stains from blood.
	""",
	4:"""
	The gray sofa at the distance which used to be a memorable place where everyone sat and enjoyed talking to one another had now become the death bed of someone you don't even know. The floor that was once a sleeping area for every celebration became a permanent sleeping area of those people. The handrail is now broken like someone had gone crazy and did despicable things. You wanted to cry. Not in agony but in fear. You are afraid that you did-No!, you know yourself more than anyone. You saw a telephone in a corner and you wanted to call the police.
	"""
	}
def main_decisions():
	return {
	0:["Call the police","Find an open door and run away","Take precautions by staying inside"],
	"Call the police":[],
	"Find an open door and run away":["Follow him","Dont follow him"],
	"Follow him":["Run", "Hide"],
	"Run":[],
	"Hide":["Call police","Go back home"], 
	"Call police":[],
	"Dont follow him":["Go in warehouse","Don't go in warehouse"],
	"Don't go in warehouse":["Sneak to the house", "Interact with them"],  
	"Interact with them":[],
	"Go back home":["Sneak to the house","Interact with them"],
	"Go in warehouse":["Take the risk and go upstairs"],
	"Sneak to the house":["Take the risk and go upstairs"],
	"Take precautions by staying inside":["Go up stairs!", "Stay there and search the area first"],
	"Go up stairs!":["Go back","Continue"],
	"Go back":["Go up stairs!", "Stay there and search the area first"],
	"Continue":["CONTINUE","NO,go back"],
	"NO,go back":[],
	"Stay there and search the area first":["Take the risk and go upstairs", "Search for alternative solution"],
	"Take the risk and go upstairs":["Go out and find another place to hide", "Stay inside and listen"],
	"Search for alternative solution":["Go out and find another place to hide", "Stay inside and listen"],
	"Go out and find another place to hide":["Approach him", "Wait for him to go"],
	"Approach him":["Do you want to follow him?", "Stay there"],
	"Stay there":["Do you want to follow him?"],
	"Do you want to follow him?":["This is it! Follow him","Go Back"],
	"This is it! Follow him":[],
	"Go Back":["Take the opposite direction", "Continue walking towards the store"],
	"Stay inside and listen":["Go out and take the risk to listen", "Stay inside the closet until the voices are gone"],
	"Wait for him to go":["You find some place to jump", "No time to jump"],
	"You find some place to jump":[],
	"No time to jump":[],
	"Take the opposite direction":[],
	"Continue walking towards the store":[],
	"Stay inside the closet until the voices are gone":[],
	"CONTINUE":[],
	}
def decision_outcome():
	return {
	"Call the police":"You decide to take the telephone and call the police. As you dial the police hotline your hand shivers in fear. You want to break down but with every remaining strength that you have you try to stand firm with your two feet. You waited for the other line to answer your call hoping that they could help you regarding your present situation. The police answered your call and you immediately told about your situation. ",

	"Find an open door and run away":"While approaching the telephone slowly, you look from side to side, trying to see if anybody is around. You slowly grab the telephone and right before you press a number, you saw a man through the window, lurking around your house. He is wearing a black cap and so, it is difficult to see his whole face. Because it is dimly lit, you can only see a portion of it. You can see he is moving his head from side to side. As if he’s looking for someone. You slowly put down the phone and lean against the wall beside the window to hide and to observe him more. You can see that he stops lurking and just quietly leaves. You are curious about him. What is he doing and who is he? Why is he creeping around your house and then would just leave like that? And so you want to do something",

	"Follow him":"You quietly approach the nearest door to get out. Without losing him in your sight, you carefully follow him. You are walking so softly, while maintaining a distance so as to not be caught by him. After a few minutes of walking just behind him, you notice he is slowing down. It seems like he can feel that he is being followed. He stopped walking and he turned his head about 45 degrees to the right. You immediately became still. You are nervous that you will get caught. You can’t move because he’ll find out. Until he looked in front again and continued to walk. But you feel so scared now. “What if he finally turns around this time and he’ll see me?” You thought to yourself.",

	"Run":"You decided to run for it. You figured he realized that he’s being followed by you. Sooner or later he’ll see you and catch you. So you are running, as fast as you can. Not even caring if he might actually see you because of that. While running, you fell on your knees. “Ouch”. But you immediately caught up and while trying to stand up, someone held your leg. You turned around to see who it was but he suddenly dragged you. You are screaming while he is dragging you by your leg ruthlessly. Your body is now full of wounds and he still wouldn’t stop. Until you saw a rock near you and you tried to get it and throw it at him. He got hit which made him let go of your leg. You took that opportunity to get up and run. While running, he grabbed your hair and hit your head with a rock. You died.",

	"Hide":"You decide not to follow him anymore. You are too scared now. So you hide under a bush for a while. “He’s tall and big, it’s not impossible that he might be carrying a weapon too. So I shouldn’t risk myself for this.” You said to yourself. “But I need to find out who he is. Maybe he can answer all my questions.” “What should I do?”",

	"Call police":"You check your body hoping that there’s a phone with you and thank god there is! You dial the hotline and right before you put the phone to your ear, it was suddenly grabbed! A person just grabbed your phone from behind! And so you immediately turned back to see him. You gasped at the sight of him. “I know this person!” “wha-what is he doing here-i-…” All these thoughts running to your mind….. And then you closed your eyes.",

	"Go back home":"“Alright, I’ll just go home. Maybe I can find more clues in that house.” You said to yourself. You courageously stood up and decided to leave him alone and just go back. You arrived at the area. But around your house, you see a group of people interacting with each other. They look serious and seem to be talking about something important. You sighed. “Uh again? Who is it this time? You told yourself.",

	"Dont follow him":"You decided to not follow him and instead you are focused on getting out of the house. You feel like the house is already too dangerous for you. You are already too scared to even put yourself in more danger. Instead of looking for that man, you headed out of the house. You thought that maybe there are neighbors who can answer your questions. And so you walked and walked, until you saw an old warehouse that seems so intriguing for you. You suddenly felt the urge to go in.",

	"Go in warehouse":"You entered the warehouse. It looks so old and rusty. And you can see the dust everywhere! You went closer and closer looking at all the things you can see. There are books, folders and papers everywhere. You saw a box and curiously took it then you saw an old computer and it caught your attention. And so you went to it and tried to maneuver it. “is this still working? Or is it broken? Should I try to open it?, you said to yourself. “Maybe I can find something from this. After all, it’s still part of my neighborhood.” And so you decided to open the computer.",

	"Don't go in warehouse":"You decided to pass through the warehouse. “It’s just a warehouse. I don’t think I can find something in there at all”, you said to yourself. You continued walking and roaming around the neighborhood until you saw a group of men. They are all wearing black caps, black jackets, and black boots. You are so curious that you decided to spy on them. When they started to walk, you also follow them. While you are following them going to a specific place, you start wondering why it feels like you are just going in circles. You observe your surroundings and thought that this is just the same place! And now you’re back to your house again! So they were headed towards your house, you figured. So what do you do next?",

	"Sneak to the house":"Investigate your own",

	"Interact with them":[],

	"Take precautions by staying inside":[],

	"Go up stairs!": "Oh! A risk taker… Are you sure about your decision?",

    "Continue":"While your legs are still trembling in fear, you decided to go upstairs for you really want to know what is written on that bracelet. It may be the answer to all the questions or most of it that keeps you unfocus and trembling in fear. As you have your first step on the stairs, you can hear the loud beat of your heart and the sound that make you make every time you took one step towards the upper floor. As you get closer and closer, your heart beats faster, and your body starting to tremble in fear more than it used to. You suddenly stop in the middle of the staircase having doubts whether to continue walking or not.",

	"CONTINUE":[],

	"Stay there and search the area first":"You silently walk back to the room where you take a quick shower, trying to find something that can be improvised as a magnifying glass. You saw an empty bottle of water, what will you do?(*Insert a game)Game: You took it and went to the bathroom. You put a small amount of water and went back to that room. You hover the bottled water at the top of the picture directly  at the bracelet. Continue...'Centro Nacional de Inteligencia' written on it with a small logo of a compass. You found the name a little bit familiar but you can't remember you saw it. You remembered that you have an old version of a computer at the study area beside your room.",
	
	"Take the risk and go upstairs":[],

    "Search for alternative solution":"You enter a room full of old books. While searching, you saw an old box with the same logo as the one in the bracelet you are wearing on that picture with the other victims. You go near the box and open it. You saw old books and old newspaper. You get one of the books and open it. However, you can't even understand what is written on it. More like its a code but the only thing that you are sure is that it is your own handwriting. You suddenly heard a siren. Who called the police? Is there anyone here besides me? Before getting trapped in this mess, you decided to:",

    "Go out and find another place to hide":[],

    "Approach him":"You decided to go out of the store and silently approach him. As you are walking towards him, he notices your shadow that makes him look up. Your eyes met one another and you saw that he slightly get shock but easily get his composure. “Follow me” he suddenly said to you like he already knows why you are there in the first place.",

    "Do you want to follow him?":"""You need answers so you decided to follow him. You thought that he will go back to his house but he didn’t. As you walk on the sidewalk, you notice that the sky is already getting darker. Aside from the sun already went down, it seems that it's going to rain. The man suddenly stop in front of an old abandoned two-storey warehouse.He look at you with intent directly in your eyes. "Come". he said coldly. """,

    "This is it! Follow him":"""You already went this far so you decided to follow him and enter that warehouse. As you step your right foot at the door,a flashing light greeted you. When your eyes already adjusted, the first thing you saw are dozens of bullets greeting you but before you lost your consciousness you saw the name “Centro Nacional de Inteligencia” wear by one of the persons who killed you and before your last breath you heard someone say, "Eliminated".""",

    "Go Back":"You suddenly get goosebumps and you instinct tells you that something bad will happen so you decided to go back. You silently turn around and run for you are afraid that he might notice that you are not following him anymore and do something bad you never want to imagine either. You are already close enough to the store where you came from when you  notice a group of people standing outside like they are waiting for someone. You get paranoid and decided to take the opposite direction but as you turn around, you notice police are just on the corner of the street taking some ronda. ",

    "Take the opposite direction":[],

    "Continue walking towards the store":"\nYou feel nervous while walking, but you are trying to maintain your composure so they won’t notice you. You feel relieved when they passed by you. You enter the shop again but this time the cashier remembers you and approaches you. She gave you a pouch saying you left it last time when you went to the store. You tried to ask her if it was during a while ago but she said it was last week. You decided to open the pouch and there you saw a piece of crumpled paper, an object suddenly hits your head rendering you unconscious. When you wake up from the loud noise of the surroundings, a young girl who is holding a picture is greeting you happily. You look around and saw that everyone who died in that accident was there happily chatting with each other. You suddenly get confused and your head is hurtin. You remembered that all of you are actually in a psychological center thus explains why you all have the same bracelet on your right hand. ",

    "Stay there":"""'I don't trust you', you said\n'Aren't you curious? Don't you want to know every thing' he replied\n'I do....but...', you said\n'Then follow me.',he said, gesturing you to go with him\nYou hesitated at first but you decided to follow him anyway.""",

    "Wait for him to go":[],

    "You find some place to jump":"You safely landed on the other surface of the house but as you turn your head a baseball bat greeted you that makes you fall unconscious and fall to death.",

	"No time to jump":[],

    "Stay inside and listen":"You started to panic. You want to hide somewhere inside that room but your curiosity also wants you to know the truth about what really happened inside that house and how did you ever involved in it in the first place. You hear footsteps getting closer and closer towards the room where you were in. You really don’t know what to do anymore. You can’t even decide properly. When the footsteps getting louder and louder adrenaline rush into your body and you quickly run to the closest closet to hide. You open the closet door and step you right foot first. However, when you are already ready to close it, you notice that the footsteps actually stop and you heard someone talking outside in a very serious tone. ",

	"Stay inside the closet until the voices are gone":"""As the voices fade out you decided to get out. You didn’t expect that someone is waiting for you outside that closet. The same as you didn’t expect that you will also meet your death. As you slowly close your eyes, you feel blood bursting out from your neck and the last thing you saw is the hand of  person walking away wearing the same bracelet engraved is the name of "Centro Nacional de Inteligencia".""",

	"Go out and take the risk to listen":"You stepped out of the closet and silently apprOached them to eavesdrop on what they are talking about. Suddenly, you stepped on something and created a noise which made the police turned back and see you. You just freezed there not knowing what to do. And then suddenly you realized that there is already a cold metal around your hands and you are already been arrested to something you didn't even do",

	"Go back":"Make a wise decision.",

	"NO,go back":"You know when you go back there's no guarantee that you'll still be alive. But you're not yet ready.",

	}
def game_cut_story():
	return {
			#Take the opposite direction text
			29: "You decided to take the opposite direction and try to hide your face from the police officers.However, one of them notice and approach you. You suddenly get scared so you run as fast as you can away from them. While catching your breath, you decided to stop and sit in the corner of the street for you think that you already went to far. It’s already dark and you decided to go back to your house wanted to sneak in and find some more clues.",
			30:	"You are walking alone, when you notice someone familiar entering a narrow alley near the opposite side of the street you always passed by when going home. You exit the shop with your groceries on hand, and decide to follow that person. The alley was slightly dark. The only source of light is an old street light at the end of the ally. As you walk closer and closer, the person was already gone. You decided to go back. However, as you turn your head, you suddenly felt dizzy and lost your consciousness.", 
			31:	"When you wake up you already saw yourself laying inside a room bounded with white wall with a table at one corner while wearing a hospital gown.",
			
			#No time to jump text
			26: "You fall As you open your eyes, everything seems so blurred.Did I hit myself so hard?you asked yourself.Then, you noticed that you are tied to a chair. You hysterically move to get out but it was so tight that it hurts every time you do it. You suddenly heard someone talking but no one's there aside from you and the darkness around you. You heard someone calling your name again and again and again but you didn't know who it is.", 
			27:	"You suddenly feel that someone is touching your shoulders and that makes you tremble in fear and thus, wanted to cry. With your remaining strength you turn your chair around but no one's there too. You feel the touch again but this time it’s like the person is trying to push you again and again. You close your eyes trying to stay strong against the pressure but you still fell on the ground-with the chair. You seem so shocked that you open your eyes and was greeted by an angry face of your mother.", 
			28:	"Shocks! I’m late!, you told yourself and get up from the floor where you fall while sleeping.",
			
			#Wait for him to go text
			22: "You wanted to approach him to ask but it's a little bit too risky especially that he may be related to the incident. You waited  for him to walk away and decided you will go inside the house hoping that no one’s there. You paid for your bill first and as you were paying the cashier gave you something that she claims you left a few weeks ago. Few weeks ago?...You asked the cashier what happened during that time.",
			23:	"Like does she even remember why you forgot that thing then she replied that you seem to be in a hurry back then for an unknown reason. You asked her if she knows where did you go next after but she replied that she didn't so you thanked her and went out of the shop. You went back to the front of the house. First, you lean your head left and right to know if someone is in there.",
			24:	"When you already secured the circumference, you approached the door and tried to open it but its lock. Then you remember some hacks on how to open a door and you tried it. You enter the house as you successfully open the door silently. You were a little bit amazed on how everything inside seems to be organized but you remember that your purpose to go there is different. You decided to search for an office first if there's any.", 
			25: "Time passes by and you seem to give up. Then, you heard someone opening the front door. You suddenly get panic. You don’t know what to do.  However, as you were trying to find some place to hide, your left foot accidentally tap a button on the ground that makes you lose your balance.The floor suddenly divided into two parts and you heard the squeak on the front door being open.",


			#CONTINUE text
			19: "You shake your head as if clearing the negative thoughts out of your mind. You take a deep breath and continue going upstairs. As you reach the second floor, you hurriedly went to your room and search if where did you put the magnifying glass. You first went to the cabinet beside your bread and open its compartment but its not there. Next, you went to the other side of the room where there is a small study table and a small box full of assorted things on the top of it.", 
			20:	"You took the box and at last, the magnifying glass was there. You took the magnifying glass and used it on the picture. While it’s slowly getting clear, you saw a text that says ““Centro National de Inteligencia”. “Why does it look familiar?” You asked yourself. But even before you remember what it is you feel cold when you realized there’s something pointed at your head. You are trying to see who this person is by just moving your eyes but the only thing you can see is the bracelet that this person is wearing that is the same as the bracelet you saw in the image.",
			21:	"Questions started to linger in your head. You thought about trying to get off from him. Right when you are about to gnash him on the stomach, you suddenly felt cold water dripping down on your face from your head. And then you are losing your balance. The last thing you hear was “Success!” ",
			
			#Take precaution text
			12: "However, you thought that it might be dangerous for you especially that you are the only one who survived this massacre. Aside from that, you own this house.'I need to solve this case on my own. No one should know'.You said to yourself and started to approach every victim to search for clues that can link them to one another. You first approached the victim near you.", 
			13:	"You are observing her physical feature-"'No, it is not a woman at all!'", you said to yourself. Its a transgender. She has an adam's apple and a more broader shoulder than a normal woman. While shivering, you took a pair of gloves and tried to touch her and yes, her body feels cold already. You tried to find out how she died but there's no sign of struggling at all. Everything was so clean.", 
			14:	"You went to the person lying on the sofa. It’s a girl with shoulder length black hair, with highlights on it. Her nose is thin that also defines her almond shaped face and a thin eyebrows and a rosy lips , She's wearing a spaghetti strap top, with a pair of tattered jeans. The same with the transgender, there is also no sign of struggling aside from the kiss mark that you noticed on her neck.", 
			15:	"You continue to observe the other victims until you notice that one of them is a child. You suddenly felt angry to someone and you don't even know who did this. The child is so young, maybe around  8-12 years old. You touch her pulse hoping that she is still alive but she isn't. You saw that the child is holding something on her right hand tightly close like she is treasuring it so much.", 
			16:	"You tried to get it wanting to know what it actually is. You successfully opened the child's hand then you saw a picture of a group of people. What shocked you the most is that it's a picture of all the victims. Including you. You are all happy. Standing in a place you don't even remember at all. Your curiosity gets deeper and deeper that you tried to find some more clues.", 
			17:	"While searching, you realize one thing that is so odd. Everyone died with no blood dripping from their bodies. However, there are blood stains everywhere. You even had blood on your clothes earlier. Where did it come from?...You asked yourself. You look at the picture again and noticed that each one of you is wearing a sort of bracelet on your left arm. There is something written in there but you can't read it for it is too small.",
			18:	"You decided to search for a magnifying glass. You wanted to go upstairs to your room but you are afraid because someone might be there watching and waiting for you.",
			
			#Go out of the house
			9:"You bring with you the clues and evidence that you have found. As you walk out of the house through the backdoor, the police have arrived already and someone is already trying to know their cause of death. You tried to eavesdrop on their conversation. While waiting for them to start a conversation, you suddenly heard someone coming so you hide on the bushes beside your house.", 
			10:"You stayed there hoping that no one will see you. However, you saw someone approaching so you decided to run. The sun is shining brightly and it was so hot that you decided to stop for a while on an abandoned warehouse near your home. You decided to take the book and analyze it. You opened the book and accidentally landed on a page where there is an address written on it. You think that it is related to what you are looking for so you decided to search for this address.",
			11:"You are now in front of a bungalow house. It doesn't look like a school though you told yourself. You decided to observe first so you went inside the grocery store across the street and sit beside the transparent window facing directly to the house. You saw someone went out. A man on his early 50's. He is wearing a blue checkered polo with a black square pants. His hair is a little bit gray already and he has a bag on his back.",
			
			#Take the risk and go upstairs text
			3:"""As you walk on the staircase you noticed that you didn't even clean it at all...You told yourself that after you solve this case you should do some proper cleaning..Anyways,you already reached the door to the study room. You open the door and went directly to the computer desk. You notice that there are some wires not connected to its specific parts. You wanted to arrange it but you need some materials to do so. So you looked around and saw a trapdoor at the ceiling. You thought that it’s connected to the attic, so in order to go there, you found a table and moved it beneath the trapdoor. Then, you put the chair on the table and tried to climb on it.""", 
	 		4:"""You successfully stand on the chair.You tried to stretch your arms in order to reach for the handle of the trapdoor. When you open it, using your own strength you pull yourself up until your butt can seat on the edge of the attic connected to the trapdoor. You decided to get up and start searching for those those materials. While searching, you saw an old box with the same logo as the one in the bracelet you are wearing on that picture with the other victims. You go near the box and open it. You saw old books and old newspaper.""",
	 		5:"""You get one of the books and open it. However, you can't even understand what is written on it. More like its a code but the only thing that you are sure is that it is your own handwriting. You took the whole box together with the other materials you needed and went down of the attic.You started to repair the broken computer but when you opened it, it ask for a password.\n\n\n Hint: 16-1-19-19-23-15-18-4""",
	 		6:"""You open the available search engine and search for "Centro Nacional de Inteligencia" hoping that it will give you some answers to your questions. Random choices pop up but it doesn't bear any logo that resembles the logo on the bracelet. While scrolling down on the list of choices you noticed that they are all actually the same. However, it's been drawn upside down. You click on one of the websites and it showed a description of a school."Be part of the growing Power that we the Centro Nacional de Inteligencia hold. As An Institution full of Knowledge and learnings that can be shared with other people.""",
	 		7:"""An aspiring school with a Goal for Aspiring  the Youth like you...Be one of us!.You seem to have found nothing important about the description so you decided to turn off the computer but you suddenly want to read the text again for you notice something useful in it. You wrote it down on a piece of paper and you tried to think outside the box until you came up with this definition."Be Part of the Power we Centro Nacional de Inteligencia hold. An Institution full of Knowledge with the Goal: Aspiring the Youth". As you read the last part, you suddenly get goosebumps all over your  body. It seems to have a double meaning.""",
			8:"""Does it inspire youths or it is the one who aspires the youth?...Whatever it is, you are very sure that it has a connection to you and to all the other victims. You decided to permanently turn off the computer now. You suddenly remembered about the box that you saw earlier. You went closer to get it but you suddenly heard a siren. Who called the police? Is there anyone here besides me? Before getting trapped in this mess, you decided to:""",
			
			#Interact with them text
			0:"So you approached them but decided to pretend to be someone else. You figured that you need to see their faces most importantly and know if they are good people or not. “Uhm, hello. Can I just ask, do you know this address? (saying the address of the warehouse from a while ago)”. You want to know if they can be trusted. Since this is your neighborhood, you are familiar with this place.",
			1:"If those men answer you correctly, then it means they are good people. “Oh, it’s actually in this area. Just go straight ahead.” Said one of the guys. “Thank you.” You replied. “So they are good people?” you asked yourself. “So should I tell them what’s inside that house?” All these questions started to linger in your head. You smiled to them and left the scene. While walking away, a lot of thoughts are running in your head.",
			2:"then suddenly a man said, “stop.”, “so it was you huh.” You turned around and looks so confused. The man grabbed your wrists and put handcuffs on you while saying, “You are under arrest for committing murder”. While he was dragging you away, you saw a man from a distance, standing beside your house. He was wearing a cap and he was looking at you, smiling."
			}