#! python3

import os
# Takes as input the name of the Surah you want added - then adds the pages of the Surah in the Correct Format to the database

# index, name, page start, page end
index_list = [
    [1, 'الفاتحة', 1, 1],
    [2, 'البقرة', 2, 49],
    [3, 'آل عمران', 50, 76],
    [4, 'النساء', 77, 106],
    [5, 'المائدة', 106, 127],
    [6, 'الأنعام', 128, 150],
    [7, 'الأعراف', 151, 176],
    [8, 'الأنفال', 177, 186],
    [9, 'التوبة', 187, 207],
    [10, 'يونس', 208, 221],
    [11, 'هود', 221, 235],
    [12, 'يوسف', 235, 248],
    [13, 'الرعد', 249, 255],
    [14, 'إبراهيم', 255, 261],
    [15, 'الحجر', 262, 267],
    [16, 'النحل', 267, 281],
    [17, 'الإسراء', 282, 293],
    [18, 'الكهف', 293, 304],
    [19, 'مريم', 305, 312],
    [20, 'طه', 312, 321],
    [21, 'الأنبياء', 322, 331],
    [22, 'الحج', 332, 341],
    [23, 'المؤمنون', 342, 349],
    [24, 'النور', 350, 359],
    [25, 'الفرقان', 359, 366],
    [26, 'الشعراء', 367, 376],
    [27, 'النمل', 377, 385],
    [28, 'القصص', 385, 396],
    [29, 'العنكبوت', 396, 404],
    [30, 'الروم', 404, 410],
    [31, 'لقمان', 411, 414],
    [32, 'السجدة', 415, 417],
    [33, 'الأحزاب', 418, 427],
    [34, 'سبأ', 428, 434],
    [35, 'فاطر', 434, 440],
    [36, 'يس', 440, 445],
    [37, 'الصافات', 446, 452],
    [38, 'ص', 453, 458],
    [39, 'الزمر', 458, 467],
    [40, 'غافر', 467, 476],
    [41, 'فصلت', 477, 482],
    [42, 'الشورى', 483, 489],
    [43, 'الزخرف', 489, 495],
    [44, 'الدخان', 496, 498],
    [45, 'الجاثية', 499, 502],
    [46, 'الأحقاف', 502, 506],
    [47, 'محمد', 507, 510],
    [48, 'الفتح', 511, 515],
    [49, 'الحجرات', 515, 517],
    [50, 'ق', 518, 520],
    [51, 'الذاريات', 520, 523],
    [52, 'الطور', 523, 525],
    [53, 'النجم', 526, 528],
    [54, 'القمر', 528, 531],
    [55, 'الرحمن', 531, 534],
    [56, 'الواقعة', 534, 537],
    [57, 'الحديد', 537, 541],
    [58, 'المجادلة', 542, 545],
    [59, 'الحشر', 545, 548],
    [60, 'الممتحنة', 548, 551],
    [61, 'الصف', 551, 552],
    [62, 'الجمعة', 553, 554],
    [63, 'المنافقون', 554, 555],
    [64, 'التغابن', 556, 557],
    [65, 'الطلاق', 558, 559],
    [66, 'التحريم', 560, 561],
    [67, 'الملك', 562, 564],
    [68, 'القلم', 564, 566],
    [69, 'الحاقة', 566, 568],
    [70, 'المعارج', 568, 570],
    [71, 'نوح', 570, 571],
    [72, 'الجن', 572, 573],
    [73, 'المزمل', 574, 575],
    [74, 'المدثر', 575, 577],
    [75, 'القيامة', 577, 578],
    [76, 'الإنسان', 578, 580],
    [77, 'المرسلات', 580, 581],
    [78, 'النبأ', 582, 583],
    [79, 'النازعات', 583, 584],
    [80, 'عبس', 585, 585],
    [81, 'التكوير', 586, 586],
    [82, 'الإنفطار', 587, 587],
    [83, 'المطففين', 587, 589],
    [84, 'الإنشقاق', 589, 589],
    [85, 'البروج', 590, 590],
    [86, 'الطارق', 591, 591],
    [87, 'الأعلى', 591, 592],
    [88, 'الغاشية', 592, 592],
    [89, 'الفجر', 593, 594],
    [90, 'البلد', 594, 594],
    [91, 'الشمس', 595, 595],
    [92, 'الليل', 595, 596],
    [93, 'الضحى', 596, 596],
    [94, 'الشرح', 596, 596],
    [95, 'التين', 597, 597],
    [96, 'العلق', 597, 597],
    [97, 'القدر', 598, 598],
    [98, 'البينة', 598, 599],
    [99, 'الزلزلة', 599, 599],
    [100, 'العاديات', 599, 600],
    [101, 'القارعة', 600, 600],
    [102, 'التكاثر', 600, 600],
    [103, 'العصر', 601, 601],
    [104, 'الهمزة', 601, 601],
    [105, 'الفيل', 601, 601],
    [106, 'قريش', 602, 602],
    [107, 'الماعون', 602, 602],
    [108, 'الكوثر', 602, 602],
    [109, 'الكافرون', 603, 603],
    [110, 'النصر', 603, 603],
    [111, 'المسد', 603, 603],
    [112, 'الإخلاص', 604, 604],
    [113, 'الفلق', 604, 604],
    [114, 'الناس', 604, 604]
]
SURAH_INDEX = 0
SURAH_NAME = 1
PAGE_START = 2
PAGE_END = 3

def main():
    """
    main function for CreateSurahBlueprint.py
    """
    print("Welcome to CreateSurahBlueprint.py")
    print("What would you like to do?")
    option_1 = ' (1) Show the list of Surahs'
    option_1 = option_1.center(211, '*')
    option_2 = ' (2) Create a Surah Blueprint'
    option_2 = option_2.center(211, '*')
    exit_prompt = ' (Type \'exit\' to exit the program) '
    exit_prompt = exit_prompt.center(211, '*')

    answer = ""

    while answer.lower() != "exit":
        print(f'{option_1}\n{option_2}\n{exit_prompt}')
        answer = input()
        if answer == "1":
            print_surah_list()
        elif answer == "2":
            print_surah_list()
            surahs_to_create = prompt_surah_blueprint()
            print(surahs_to_create)
            if len(surahs_to_create) > 0:
                create_surah_blueprint(surahs_to_create)

def print_surah_list():
    """
    Prints the list of Surahs
    """
    print("Here is the list of Surahs:")
    print("Index".ljust(10) + "Name".ljust(30) + "Page Start".ljust(20) + "Page End".ljust(20))
    for surah in index_list:
         # Encode each string before printing
        index = str(surah[0]).encode('utf-8', 'ignore').decode('utf-8')
        name = surah[1].encode('utf-8', 'ignore').decode('utf-8')
        page_start = str(surah[2]).encode('utf-8', 'ignore').decode('utf-8')
        page_end = str(surah[3]).encode('utf-8', 'ignore').decode('utf-8')

        print(index.ljust(10) + name.ljust(30) + page_start.ljust(20) + page_end.ljust(20))

def prompt_surah_blueprint():
    """
    Prompts the user for the Surah Blueprint, returning a list of Surah indices to create
    """
    try:
        print("What is the index of the Surah you would like to add?\nInput either an index (e.g. 1) or a range of indices (e.g. 1-5)")
        surah_index = input()
        surah_index = surah_index.split('-')
        if len(surah_index) == 1:
            surah_index = int(surah_index[0])
            print(f"You have chosen Surah {index_list[surah_index-1][1]}. Is that right? (y/n)")
            answer = input()
            if answer == "y":
                return [surah_index-1]
            else:
                return []

        elif len(surah_index) == 2:
            surah_index = [int(surah_index[0]), int(surah_index[1])]
            print(f"You have chosen Surahs {index_list[surah_index[0]-1][1]} to {index_list[surah_index[1]-1][1]}. Is that right? (y/n)")
            answer = input()
            if answer == "y":
                return list(range(surah_index[0]-1, surah_index[1]))
            else:
                return []
        else:
            print("Invalid input. Please try again.")
            return []
    except Exception:
        print(f"Invalid input. Please try again.")
        return []

def create_surah_blueprint(surahs_to_create):
    """
    Creates Surah Blueprints for the Surahs specified
    """
    current_directory = os.getcwd()
    blueprint_folder = os.path.join(current_directory, "SurahBlueprints")
    if not os.path.exists(blueprint_folder):
        os.makedirs(blueprint_folder)
    print("Going to create the following Surah Blueprints:")
    for surah_index in surahs_to_create:
        surah = index_list[surah_index]
        number_pages = surah[PAGE_END] - surah[PAGE_START] + 1
        print(f"**Surah {surah[SURAH_NAME]} ({number_pages} pages)**")
        for i in range(number_pages):
            filename = f"{surah[SURAH_INDEX]}- سورة {surah[SURAH_NAME]}"
            extension = f"({i+1}).md"
            filename += extension
            print(filename)
    print("Continue? (y/n)")
    answer = input()
    if answer == "y":
        for surah_index in surahs_to_create:
            surah = index_list[surah_index]
            number_pages = surah[PAGE_END] - surah[PAGE_START] + 1
            for i in range(number_pages):
                filename = f"{surah[SURAH_INDEX]}- سورة {surah[SURAH_NAME]}"
                extension = f"({i+1}).md"
                filename += extension
                with open(os.path.join(blueprint_folder, filename), "w", encoding="utf-8") as f:
                    f.write(f"---\n")
                    f.write(f"title: \"{surah[SURAH_NAME]}\"\n")
                    f.write(f"number: {surah[SURAH_INDEX]}\n")
                    f.write(f"page: {surah[PAGE_START] + i}\n")
                    f.write(f"---\n")
                    f.write(f"\n")
                    f.write(f"## {surah[SURAH_NAME]} - Page {surah[PAGE_START] + i}\n")
        print("Surah Blueprints created successfully!")
    else:
        return

if __name__ == "__main__":
    main()