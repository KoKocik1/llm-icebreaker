from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# import os

information = """
    Elon Reeve Musk (wym. /ˈi:lɒn ˈmʌsk/; ur. 28 czerwca 1971 w Pretorii[4]) – południowoafrykański przedsiębiorca, założyciel lub współzałożyciel przedsiębiorstw SpaceX, Tesla, Neuralink, X.com (część firmy PayPal) i The Boring Company[5]. Pochodzi z Republiki Południowej Afryki, mieszka i pracuje w Stanach Zjednoczonych (posiada obywatelstwo południowoafrykańskie, kanadyjskie oraz amerykańskie). Dyrektor generalny i techniczny w SpaceX, dyrektor generalny i główny architekt w Tesla Inc. W styczniu 2021 został uznany najbogatszym człowiekiem świata przez magazyn „Forbes” i agencję Bloomberg﻿[w innych językach][6][7][8]. Od 28 października 2022 właściciel serwisu X (kiedyś „Twitter”). Od 20 stycznia 2025 szef Departamentu Wydajności Rządu﻿[w innych językach] (Department of Government Efficiency, DOGE) w drugim gabinecie Donalda Trumpa.

Życiorys
Dzieciństwo i edukacja
Pochodzi z Południowej Afryki[9]. Urodził się i wychował w stołecznej Pretorii, w białej rodzinie. Jego ojciec, inżynier Errol Musk, urodził się w Południowej Afryce jako syn Brytyjki i Południowoafrykańczyka, natomiast matka, modelka i dietetyczka Maye Musk, ma po ojcu amerykańskie pochodzenie i przyszła na świat w Kanadzie[10][11]. W 1950 wyjechała z rodzicami do Południowej Afryki[10]. Elon ma dwoje młodszego rodzeństwa: brata Kimbala i siostrę Toscę[11].

Po rozwodzie rodziców w 1980 Elon mieszkał głównie z ojcem[10]. Kiedy miał 10 lat, dostał pierwszy komputer i nauczył się programować[12]. Dwa lata później sprzedał swój pierwszy program – grę komputerową Blastar za około 500 dolarów[12].

Jako nastolatek uczęszczał do Pretoria Boys High School, którą ukończył w wieku 17 lat. Krótko później, częściowo z chęci uniknięcia obowiązkowej służby wojskowej w Południowoafrykańskich Siłach Obronnych (SADF), wyemigrował do Kanady, gdzie mieszkała rodzina jego matki[12]. Planował przeniesienie się do Stanów Zjednoczonych[13][14].

W Kanadzie pracował u kuzyna na farmie w Swift Current, przy czyszczeniu kotłów w tartaku w Kolumbii Brytyjskiej i przy wyrębie lasów. Po dwóch latach przeniósł się do Toronto i pracował w dziale IT w banku, aplikując jednocześnie do Queen’s University. Opuścił Kanadę w 1992 roku po uzyskaniu stypendium na University of Pennsylvania. Tam uzyskał tytuł licencjata w dziedzinie ekonomii na wydziale Wharton Business School, po czym studiował tam jeszcze rok uzyskując tytuł licencjata w dziedzinie fizyki[15].
"""
if __name__ == "__main__":
    print("Hello, World!")
    # print(os.environ['OPEN_API_KEY'])

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. a short summary
        2. a list of 2-3 interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    chain = summary_prompt_template | llm

    res = chain.invoke({"information": information})

    print(res)
