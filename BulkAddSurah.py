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
def main():
    """
    main function for BulkAddSurah.py
    """
    # print("Welcome to BulkAddSurah.py")
    # print("This program will add the pages of a Surah to the database")
    # print("Please enter the name of the Surah you want to add")
    # surahName = input()
    # print("You have entered: " + surahName)
    # print("Is this correct? (Y/N)")
    # confirmation = input()
    # if confirmation == "Y":
    #     print("Adding Surah to Database")
    #     addSurah(surahName)
    # else:
    #     return
    

if __name__ == "__main__":
    main()