
# - @HAHAHA_DECOD
#2025-05-27
#ZAXOTEL MADE

import os
import subprocess
from colorama import init, Fore, Style
import time
import threading

init(autoreset=True)

def clear():
    os.system("clear")

def spinner():
    while running:
        for symbol in ["""
@@@@@@@@@#@@@@@@@@@@@@@?%@@S%S##@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#S???*+,..,::::;*%S#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@S*+;:::,......,,,,:::,;+S@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@?+:.,::,..,,.......,.,,:++#@@@@@@@@@@@@@@
@@#@@@@@@@@@#*;:,:,:,...,:..:,..,::,;:;;*@@@@@@@@@@@@@@
@@@@@@@@@@@#*;,,:,::,,,..:,.,:,.,::,::::;S@@@@@@@@@@@@@
@@@S*+;:;+;:,;;,,,,:,,,;:.::,:,,,:*%@@@@@@@@@@@@@@@@@@@
@@S%**++*+:,:;;::,.,:,,:+::;,:,,,;+*##SS###@@@@@@@@@@@@
@@#@@@@@@@*?*;;:,::,..:++:::,,,,,;;:;:..:*;?@@@@@@@@@@@
@@@@@@@@@#*?;:;;;:,.,,,::*;++::.,,:;;;,,;;:+@@@@@@@@@@@
@@@@@@@@@S+*,,++,...,,,..,,:;+,::::;??+++,:;@@@@@@@@@@@
@@#@@@@@@#*?::++:;*?%%;...,,.,,*%%+;;*%?+:,;@@@@@@@@@@@
@@@@@@@@@@+*+,,+;,:++:..........,,...:??*+,*@@@@@@@@@@@
@@#@@@@@@@**?:,??:..................,**+*::#@@@@@@@@@@@
@@#@@@@@@@#S+:;?*,................,:*?+;*+?@@@@@@@@@@@@
@@@@@@@@@@@@*:+**,...............:+?*;;;:%@@@@@@@@@@@@@
@@@@@@@@@@@@@#???;,.............,*%?**+,+@@@@#@@@@@@@@@
@@@@@@@@@@@@@@#?+;;,...........,+*+:;+;*@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#++*::;+,......,::?*;,;??@@@@@@@@@@@@@@@@
@@#@@@@@@@@@@@S;:;:+#*.......;#++*+::+#@@@@@@@@@@@@@@@@
@@#@@@@@@@@@@@S??%?S@%*******%@#?;:::+S@@#?****?#@@@S%%
@@@@@@@@@@@@@?+*%#@@@@@@%+*S@@@@@%*:::+S@@S%%%%S@@@@#SS
@@@@@@@@@@@@@;:*S@@@@@@#%?%S@#@@@@S%+,:#@@@@@@@@@@@@@@@""", """
@@@@@@@@@@@@@@@@@@@@@@@%?#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@##%*%*;:::;+*%#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#%*+:,::,..,::,,,,::;*?S@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@S*:.,,:,,..,.......,,,,;+*@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%+;,::::,..,:.,:,..,:,,,,;;?@@@@@@@@@@@@@@
@@@@@@@@@@@@?+:,:::;,,,.,:,.,:,..:,,:,::;S@@@@@@@@@@@@@
@@@@@@@@@@@?+:.:;;:,:;:,.,:,.,;,.,:,:,,,:?#@@@@@@@@@@@@
@@@@@@@@@@S++::;;,.,;+::,.,::,:*;:+::,..:**@@@@@@@@@@@@
@@@@@@@@@@***;;;,,::,,;++,:,,.,:;+;;+:..:*;%@@@@@@@@@@@
@@@@@@@@@#*?+::;:;,...,;++;+;::,,,;::;,,++;+@@@@@@@@@@@
@@@@@@@@@#*?:,++:,.......;:;++,,,,,;?*;;*::;@@@@@@@@@@@
@@@@@@@@@#*?,:++,:;+*?;,..,,,::?%%*+*?%*+:,;@@@@@@@@@@@
@@@@@@@@@@+?;::+;:;??+,....,...,;;,..;%?*+,*@@@@@@@@@@@
@@@@@@@@@@**?:,*?:..................,+*+*;:S@@@@@@@@@@@
@@@@@@@@@@#S*::%?:.................,+?*;?;*@@@@@@@@@@@@
@@@@@@@@@@@@+,+?*................,;*?+:+;?@@@@@@@@@@@@@
@@@@@@@@@@@@#S??%:..............,+%%**+::#@@@@@@@@@@@@@
@@@@@@@@@@@@@@S%*;;,,..........,+??+++;;#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#++*;::;.......,,:??;,;?*#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@+;;:+#?.......;S;*?+::?#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@?,::;?@?:......+@#*+;;:;?@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%,::+#@@@#%;,,;%@@@@S*;;,:%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@*,+%@@@@@@@S*?#@@@@@@#?*,,%@@@@@@@@@@@@@@@""","""
@@@@@@@@@@@@@@@@@@@@@@@@SS@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#*%#%???%S#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@#S?**+;;,.,,,,,:;*?S#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%;,,,,,....,,,,.,,,,,:+*#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*:,,::,...,,..,....,...,;+S@@@@@@@@@@@@@@
@@@@@@@@@@@@S;,.::::,,,.,:,,:,...:,.:.,;+#@@@@@@@@@@@@@
@@@@@@@@@@@%;,,::::,:+,..::..,:,.::.:,.:;*@@@@@@@@@@@@@
@@@@@@@@@@S:,.,;::,,++:,..::,.,;,,+,:,..:+*@@@@@@@@@@@@
@@@@@@@@@@*;::;:,,::,,;+;..,,..:;+;;;,..,+;S@@@@@@@@@@@
@@@@@@@@@#+*:;:::;,...:++;,::,:,,::::+,.:;:+@@@@@@@@@@@
@@@@@@@@@S+*:,+*:,..,,.,.::;*;:....,::::+:,:#@@@@@@@@@@
@@@@@@@@@S+*,:**,,,,:;:,..,::*+*??*+*%?**:::#@@@@@@@@@@
@@@@@@@@@#;+::;++:;?%%;....,..,:**;,,;S?+;::@@@@@@@@@@@
@@@@@@@@@@;+?,,*%:.,,,...............:**+*,*@@@@@@@@@@@
@@@@@@@@@@S%?+,?S;,................,:+*;+;:#@@@@@@@@@@@
@@@@@@@@@@@@*::+?,...............,;+*+;*+;%@@@@@@@@@@@@
@@@@@@@@@@@@#??+%;...............:+*?**+,%@@@@@@@@@@@@@
@@@@@@@@@@@@@@#?*;+,............:;**+;;:?@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@+:*+:,:,.......,,+*+,:*+%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@+:;:;?S,......:S;+%+::*S@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@?:,:++#S:......;@#+;;;:;?@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%,:,;S@@@#%+,,;?#@@@S*;;,;%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@+,;?@@@@@@@S*?#@@@@@@#?+,,%@@@@@@@@@@@@@@@""", """
@@@@@@@@@@@@@@@@@@@@@@@@S%S@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@??#@S%SSS#####@@@@@@@@@@@@@@@@@@
@#@@@@@@@@@@@@@@@@@@@#S%?*+;:,.,,::::;;*?SS@@@@@@@@@@@@
@@@@@@@@@@@@@@@%%?+++::........,,.,::;;+%##@@@@@@@@@@@@
@@@@@@@@@@@@@#?+:,,,,,...,,.,...,,...,;;S@@@@@@@@@@@@@@
@@@@@@@@@@@@#+,,::,:,...,:,.::...:,.:,,;+#@@@@@@@@@@@@@
@@@@@@@@@@@S;,,:::;:,::..::..::,.,:.:,.,;*#@@@@@@@@@@@@
@@@@@@@@@@#;,.,:;:,,;++:..,:,.:+::+,,:..,;+#@@@@@@@@@@@
@@@@@@@@@@?:,,;:,.,:::;;;,.,,,,:;+::::...::?@@@@@@@@@@@
@@@@@@@@@@+;:;:::::,..,+*+:,:,::.,;;:+,.,::;@@@@@@@@@@@
@@@@@@@@@#;:,,;*:,..,,.,;;;;*;::,..:+;;,;:::#@@@@@@@@@@
@@@@@@@@@S;:.,+*:,,:;+;,..,::;;*??*+?%%*?::,#@@@@@@@@@@
@@@@@@@@@S,:,::**:;?%%;,...,...,**;,.:%**+,:@@@@@@@@@@@
@@@??%+*SS,,,,.,:,..,,.......,::,+,,*%####%S@@@@@@@@@@@
@@@%+*+:S%:,...,,...........,:++;*::@@@@@@@@@@@@@@@@@@@
@@@@%@@@@@@#*,:*?,...............,:+?*;***%@@@@@@@@@@@@
@@@@S@@@@@@@#%?+S+,..............,+**+?*,%@@@@@@@@@@@@@
@@@S@@@@@@@@@@#?*;+,,..........,:;?++++:%@@@@@@@@@@@@@@
@@@?SSS@@@@@@@@+:++:,;,.......,,***,:++S@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@+:;;;%#,......,S+;%*::+S@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@?:,,+*@%:......;@#*;;+:;?@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%,::+S@@@#%+,,;?#@@@S+;;,:%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@*,;%@@@@@##S?%S#@@@@@#?+,,%@@@@@@@@@@@@@@@""", """
@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@?+%#SSS##@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@##S?*?;;:,,,:::;+*?S#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%*+:,,,,,...:,,,,,,,::+*?@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%*;::::,...,,.,....,..,,;;?@@@@@@@@@@@@@@
@@@@@@@@@@@@#*:,,:,::,..,:,,::...::,,,,;+S@@@@@@@@@@@@@
@@@@@@@@@@@#+,.:::;;,::,.::..::,.,:,::.,;+S@@@@@@@@@@@@
@#@@@@@@@@@*:.,:;;:,;*+:,,::,.:+:,;:,:..,;+S@@@@@@@@@@@
@@@@@@@@@@%;,,;;:,,:::;;;,.,:,,:++;;::,..:;*@@@@@@@@@@@
@@@@@@@@@@*;:;;::::,,.,+*+:,:,,:.,;;:+,.,::;S@@@@@@@@@@
@@@@@@@@@#+;::;+;:,.,,,,+++:*;::,,.:+;;,:;::?#S@@@@@@@@
@@@@@@@@@S;:,,;*:.,,,::,.,,;;+;+*++;*%%**;:,?@@@@@@@@@@
@@@@@@@@@S::,:;**;;?%S*,...,..,:?%*:::%%?+:,%@@@@@@@@@@
@@@@@@@@@#;:;:,;%;.,;:,..............,+*+?::#@@@@@@@@@@
@@@@@@@@@@S+++,+S+,.................,;*++?,+@@@@@@@@@@@
@@@@@@@@@@@#*::*%:................,;**+;**+%@@@@@@@@@@@
@@@@@@@@@@%%#*??S*:::,,,,........,:++++?:;@@@@##@@@@@@@
@@@@@@@@@@@@@@@@@@@@@S?*;;,............,:*?+++:+@@@@@@@
@@@@@@@@@@@@@@@%??%?**;,,:,,..,,:;;,,:;*S#SSS#S#@@@@@@@
@@@@@@@@@@@@@@@*:;;:+%:.......*+;??;,+?#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@S;,:;+SS,......,S#++++:;?@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#:,::?#@@S*:..,;%@@#%++;:;%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@?,:+#@@@@@@#*+S@@@@@@#*+,,+%@@@@@@@@@@@@@@""", """
@@@@@@@@@@@@@@@@@@@@@@@?%S%?*?%%S#@@@@@@@@@@@#@@@@@@@@@
@@@@@@@@@@@@@@@@#S%*+;+;:,,,,,,,,:;*?S#@@@@@@#@@@@@@@@@
@@@@@@@@@@@@@@@%;,..,,,...,,,...,,,,:;+?@@@@@#@@@@@@@@@
@@@@@@@@@@@@@#*+:,,::,...:..,....,,.,,;;*@@@@#@@@@@@@@@
@@@@@@@@@@@@S+;,,:,:,.,..:,.,:,..,,,:,,::S@@@#@@@@@@@@@
@@@@@@@@@@@S+;,,::::,::..,:,.,:,.,:,::,::*#@@#@@@@@@@@@
@@@@@@@@@@#++:,:;:,.:+::,.,:,,:+:,;:,,..,**#@#@@@@@@@@@
@@@@@@@@@@?+*;;;,.,::,:;;,,,,,.:;;:;;:..,*;?@#@@@@@@@@@
@@@@@@@@@@*?*;;::::,..,;++:;:,:,.,;::;,.:+;;##@@@@@@@@@
@@@@@@@@@#**;,;+:,.......;:;*;:.,,.:++;:+:::S#@@@@@@@@@
@@@@@@@@@#**:,++,,:;;+;,..,,,;:+???+*??**,::S@@@@@@@@@@
@@@@@@@@@@**;,:;;:;?%?:....,...,++:..:??*+,:##@@@@@@@@@
@@@@@@@@@@?+%:,+?:.,,................:*+*;,?@#@@@@@@@@@
@@@@@@@@@@#%?;:*?;,................,:**;++;#@@@@@@@@@@@
@@@@@@@@@@@@*,:**,...............,:+?+:;;+#@@@@@@@@@@@@
@@@@@@@@@@@@#%?+%;...............;?%*++:,%@@@#@@@@@@@@@
@@@@@@@@@@@@@@#??;;,............;*?+++;:%@@@@#@@@@@@@@@
@@@@@@@@@@@@@@@*;*;:,;,.......,,*?+,:**S@@@@@#@@@@@@@@@
@@@@@@@@@@@@@@@*:;:;%%,......:%+;*+::*S@@@@@@#@@@@@@@@@
@@@@@@@@@@@@@@?,,:;*#?:......;##+;;;:;?@@@@@@#@@@@@@@@@
@@@@@@@@@@@@@%,,:+S@#@#?;,,;?##@@S*::,:%@@@@@#@@@@@@@@@
@@@@@@@@@@@@@*,+%@@###@@S**S@@#@@@S?*,,%@@@@@#@@@@@@@@@""", """
@@@@@@@@@@@@@@@@@@@@@@@++%%**??%S#@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#%?*;;;::,.,,,,,:;;*%S#@@@@@@@@@@@@@@@#
#@@@@@@@@@@@@@#?*:,,,,,...,,,...,,,,:++?@@@@@@@@@@@@@@@
#@@@@@@@@@@@@S*;:::::,..,:,,,...,:,.,,;;%@@@@@@@@@@@@@@
@@@@@@@@@@@@S;,,::::,,,.,:,,::..,::,:,,;+S@@@@@@@@@@@@@
@@@@@@@@@@@%;,,::;;::;:,,::,.::,.,:,:,,,;*#@@@@@@@@@@@@
@@@@@@@@@@%;,,:;;:,,+++:..::,,:+:;;,,,..,;*@@@@@@@@@@@@
@@@@@@@@@#*:,:;:,,::,,;;;,.,,,,:;;:;;:..,:;%@@@@@@@@@@@
@@@@@@@@@S+;:;:;:::,..:**+:::,:,.,;;;;,.:::*@@@@@@@@@@@
@@@@@@@@@%;:,,++:,..,,.,;;;**;::,..;++;:+::;@@@@@@@@@@@
@@@@@@@@@%;:,:*+,,:;++;,..,::;;?%%*+?%%?*::;@@@@@@@@@@@
@@@@@@@@@?::::;*+:;?%?:....,...:++,,.;%?*;,+@@@@@@@@@@@
@@@@@@@@@#;;+:,?%:.,,...............,;*;?;,%@@@@@@@@@@@
@@@@@@@@@@S?+;:??:.................,;*++?;:#@@@@@@@@@@@
@@@@@@@@@@@#+:+??,...............,;**+;*+?%@@@@@@@@@@@@
@@@@@@@@@@@@S%*?%;,.............,:*?**?;:#@@@@@@@@@@@@#
@@@@@@@@@@@@@@S?;++,,..........,:+?++*+;#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#;;+;::;.......,,:*?+,;**#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@S;:;;+#?.......;S;+?+::*S@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#+,,:+%@?,.....,*@#*;++:+%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@*,::*#@@@#?;.:+S@@@@S++:,;#@@@@@@@@@@@@@@@
@@@@@@@@@@@@#;,+S@@@@@@@S?S#@@@@@@S?;,:#@@@@@@@@@@@@@@@""", """
@@@@@@@@@@@@@@@@@@@@@@@?+%#SSS##@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@##S?*?;;:,,,:::;+*?S#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%*+:,,,,,...:,,,,,,,::+*?@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%*;::::,...,,.,....,..,,;;?@@@@@@@@@@@@@@
@@@@@@@@@@@@#*:,,:,::,..,:,,::...::,,,,;+S@@@@@@@@@@@@@
@@@@@@@@@@@#+,.:::;;,::,.::..::,.,:,::.,;+S@@@@@@@@@@@@
@#@@@@@@@@@*:.,:;;:,;*+:,,::,.:+:,;:,:..,;+S@@@@@@@@@@@
@@@@@@@@@@%;,,;;:,,:::;;;,.,:,,:++;;::,..:;*@@@@@@@@@@@
@@@@@@@@@@*;:;;::::,,.,+*+:,:,,:.,;;:+,.,::;S@@@@@@@@@@
@@@@@@@@@#+;::;+;:,.,,,,+++:*;::,,.:+;;,:;::?#S@@@@@@@@
@@@@@@@@@S;:,,;*:.,,,::,.,,;;+;+*++;*%%**;:,?@@@@@@@@@@
@@@@@@@@@S::,:;**;;?%S*,...,..,:?%*:::%%?+:,%@@@@@@@@@@
@@@@@@@@@#;:;:,;%;.,;:,..............,+*+?::#@@@@@@@@@@
@@@@@@@@@@S+++,+S+,.................,;*++?,+@@@@@@@@@@@
@@@@@@@@@@@#*::*%:................,;**+;**+%@@@@@@@@@@@
@@@@@@@@@@%%#*??S*:::,,,,........,:++++?:;@@@@##@@@@@@@
@@@@@@@@@@@@@@@@@@@@@S?*;;,............,:*?+++:+@@@@@@@
@@@@@@@@@@@@@@@%??%?**;,,:,,..,,:;;,,:;*S#SSS#S#@@@@@@@
@@@@@@@@@@@@@@@*:;;:+%:.......*+;??;,+?#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@S;,:;+SS,......,S#++++:;?@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#:,::?#@@S*:..,;%@@#%++;:;%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@?,:+#@@@@@@#*+S@@@@@@#*+,,+%@@@@@@@@@@@@@@"""]:
            print(Fore.BLUE + Style.BRIGHT + "@@@ Ищем данные по запросу, не завершайте сессию...@@@@" + f'\r{symbol}' + Fore.WHITE, end='', flush=True)
            time.sleep(0.08)
            clear()

if not os.path.exists('databases'):
    print(f"   не удается найти папку 'databases'")
else:
    count = len(os.listdir('databases'))
    print(f'   Количество баз данных: {count}.\n')
    data = input(f'   введите запрос: ')
    
    result = ''
    running = True

    # Запуск анимации в отдельном потоке
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.start()

    for label in os.listdir('databases'):
        file_path = os.path.join('databases', label)
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                for line in f:
                    if data in line:
                        result += f"[{label}] - {line}".replace('.', '').replace('[', '').replace(']', '').replace('"', '').replace('NULL', '')
                        break
        except Exception as e:
            print("")
    
    running = False  # Остановка анимации
    spinner_thread.join()  # Дожидаемся завершения потока с анимацией

    print('\nПроцесс завершен.')
    
    if result:
        print('\nВот что мы нашли:\n')
        print(result)
    else:
        print(Fore.BLUE + "Ничего не найдено")

    input("Нажмите enter... " + Style.RESET_ALL)
    
    os.system("clear")
    subprocess.run(["python", "main.py"])