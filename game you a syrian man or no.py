print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ████████╗██╗░░██╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ░░░██║░░░███████║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝
""")

print("If you are from Syria, you must answer these questions.")
syrian_1 = input("If you are Syrian, would you break your fast with liver and beans or cheese and labneh with a cup of tea?  'yes','no' \n ").lower()

if syrian_1 == 'yes':
    print("Good! Correct answer but! This does not mean that you are Syrian")
elif syrian_1 == 'no':
    print("Your answer is wrong! But that doesn't mean you're not Syrian.")

syrian_2 = input("If you are Syrian, after breakfast, do you drink Turkish coffee V60? 'yes' 'no'\n ").lower()

if syrian_2 == 'yes':
    print("Good! This is your second answer, but that doesn't mean you're Syrian. You still have an answer.")
elif syrian_2 == 'no':
    print("God alone, you are not Syrian, but try, it's okay")

syrian_3 = input("If you are Syrian, when you drink coffee, do you listen to Fairuz or Nancy? 'yes' 'no'\n").lower()

if syrian_3 == 'yes':
    print("Good, you are Syrian, but let me ask you one last question so we can know if you are Syrian from your father and grandfather.")
elif syrian_3 == 'no':
    print("You have one last answer to convince me that you are Syrian, but your information is not good")

syrian_4 = input("If you are Syrian, does your mother clean the room wall? 'yes' 'no'\n").lower()

if syrian_4 == 'yes':
    print("Gooood! passed the test")
elif syrian_4 == 'no':
    print("Sorry I failed")
