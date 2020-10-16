# Ultimate Stamina RPG Stat Tracking Project
# Personal project to use what I've learned in Python to output stats

import csv

# Declaring variables
Scores = {}
TotalFantastics = [0] * 16
TotalExcellents = [0] * 16
TotalGreats = [0] * 16
TotalDecents = [0] * 16
TotalWayOffs = [0] * 16
TotalMisses = [0] * 16
TotalSongsPerDiff = [0] * 16
TotalFullCombos = [0] * 16

# Open up the csv file and dump each row to a dictionary
# Dictionary key is the song difficulty and the song title in order to weed out the same song with multiple diffs
# Each key is then paired with an indexed list to store various data points about it
with open('srpgscores.txt', mode='r') as csv_file:
    ScoresCSV = csv.DictReader(csv_file)
    line_count = 0
    for row in ScoresCSV:
        Scores[f'[{row["SongDifficulty"]}] - {row["SongTitle"]}'] = [int(row["SongDifficulty"]), int(row["SongBPM"]),
                                                                     row["ScorePassBool"], float(row["ScoreValue"]),
                                                                     row["ScoreDate"], int(row["ScoreFantastic"]),
                                                                     int(row["ScoreExcellent"]), int(row["ScoreGreat"]),
                                                                     int(row["ScoreDecent"]),
                                                                     int(row["ScoreWayOff"]), int(row["ScoreMiss"])]
        line_count += 1
    print(f'Processed {line_count} scores.\n')
    csv_file.close()

# Pull key value from dictionary(song difficulty and title) and display the stats for each key
for item in Scores.items():
    print(
        f"{item[0]} - {item[1][1]} BPM\n"
        f"Passed with a {item[1][3]}% on {item[1][4]}\n"
        f"\t\tFantastic Count: {item[1][5]}\n"
        f"\t\tExcellent Count: {item[1][6]}\n"
        f"\t\tGreat Count: {item[1][7]}\n"
        f"\t\tDecent Count: {item[1][8]}\n"
        f"\t\tWay Off Count: {item[1][9]}\n"
        f"\t\tMiss Count: {item[1][10]}\n"
    )
    # Adding currently pulled song's judgements to the overall total judgement count (index 0)
    TotalFantastics[0] += item[1][5]
    TotalExcellents[0] += item[1][6]
    TotalGreats[0] += item[1][7]
    TotalDecents[0] += item[1][8]
    TotalWayOffs[0] += item[1][9]
    TotalMisses[0] += item[1][10]
    TotalSongsPerDiff[0] += 1
    # If block level is a certain number, write the judgements to the correct index within the various judgement lists
    # Check if Decent, Way Off, and Misses are all 0 to indicate a full combo
    if item[1][8] == 0 and item[1][9] == 0 and item[1][10] == 0:
        TotalFullCombos[0] += 1
        for CurrentBlockDif in range(1, 15):
            if item[1][0] == 10 + CurrentBlockDif:
                TotalFullCombos[CurrentBlockDif] += 1
    # Go through 15 times and check the block difficulty of the song with the current iteration+10
    # We check current iteration+10 since difficulties start at 11
    # If the current iteration+10 matches the song's block difficulty, write the judgement values
    for CurrentBlockDif in range(1, 15):
        if item[1][0] == 10 + CurrentBlockDif:
            TotalFantastics[CurrentBlockDif] += item[1][5]
            TotalExcellents[CurrentBlockDif] += item[1][6]
            TotalGreats[CurrentBlockDif] += item[1][7]
            TotalDecents[CurrentBlockDif] += item[1][8]
            TotalWayOffs[CurrentBlockDif] += item[1][9]
            TotalMisses[CurrentBlockDif] += item[1][10]
            TotalSongsPerDiff[CurrentBlockDif] += 1

# Add up all the judgement counts without misses for the total hits, then add misses
# Divide the total hits by the total overall count to get a percentage of notes hit
# Then convert to a string and slice string to display in the xx.xx% format
TotalOverallHits = TotalFantastics[0] + TotalExcellents[0] + TotalGreats[0] + TotalDecents[0] + TotalWayOffs[0]
TotalOverallCount = TotalOverallHits + TotalMisses[0]
TotalOverallPercent = TotalOverallHits / TotalOverallCount
TotalOverallPercentString = str(TotalOverallPercent)
TOPSOne = TotalOverallPercentString[2:4]
TOPSTwo = TotalOverallPercentString[4:6]

# Display the total judgement counts overall
print(
    "O V E R A L L  S T A T S\n"
    "========================\n"
    f"Total notes hit: {TotalOverallHits}/{TotalOverallCount}\n"
    f"{TOPSOne}.{TOPSTwo}% notes hit over {TotalSongsPerDiff[0]} songs\n"
    f"{TotalFullCombos[0]} full combos\n"
    f"Total Fantastics: {TotalFantastics[0]}\n"
    f"Total Excellents: {TotalExcellents[0]}\n"
    f"Total Greats: {TotalGreats[0]}\n"
    f"Total Decents: {TotalDecents[0]}\n"
    f"Total Way Offs: {TotalWayOffs[0]}\n"
    f"Total Misses: {TotalMisses[0]}\n"
    )

# Display the judgement counts for each difficulty

# Go through 15 times (11-25) and print out the stats for the block difficulty if a song has been passed
# Current block is 10 + current iteration (1st iteration = 11, 2nd iteration = 12, 3rd = 13, etc.)
for CurrentBlockDif in range(1, 15):
    if TotalSongsPerDiff[int(CurrentBlockDif)] >= 1:
        print(
            f"[{10 + int(CurrentBlockDif)}] - {TotalSongsPerDiff[int(CurrentBlockDif)]} Songs\n"
            f"{TotalFullCombos[int(CurrentBlockDif)]} full combos\n"
            "========================\n"
            f"Total Fantastics: {TotalFantastics[int(CurrentBlockDif)]}\n"
            f"Total Excellents: {TotalExcellents[int(CurrentBlockDif)]}\n"
            f"Total Greats: {TotalGreats[int(CurrentBlockDif)]}\n"
            f"Total Decents: {TotalDecents[int(CurrentBlockDif)]}\n"
            f"Total Way Offs: {TotalWayOffs[int(CurrentBlockDif)]}\n"
            f"Total Misses: {TotalMisses[int(CurrentBlockDif)]}\n"
        )


# Old code
# print(
#     f"[11] - {TotalSongsPerDiff[1]} Songs\n"
#     f"{TotalFullCombos[1]} full combos\n"
#     "========================\n"
#     f"Total Fantastics: {TotalFantastics[1]}\n"
#     f"Total Excellents: {TotalExcellents[1]}\n"
#     f"Total Greats: {TotalGreats[1]}\n"
#     f"Total Decents: {TotalDecents[1]}\n"
#     f"Total Way Offs: {TotalWayOffs[1]}\n"
#     f"Total Misses: {TotalMisses[1]}\n"
#     )
#
# print(
#     f"[12] - {TotalSongsPerDiff[2]} Songs\n"
#     f"{TotalFullCombos[2]} full combos\n"
#     "========================\n"
#     f"Total Fantastics: {TotalFantastics[2]}\n"
#     f"Total Excellents: {TotalExcellents[2]}\n"
#     f"Total Greats: {TotalGreats[2]}\n"
#     f"Total Decents: {TotalDecents[2]}\n"
#     f"Total Way Offs: {TotalWayOffs[2]}\n"
#     f"Total Misses: {TotalMisses[2]}\n"
#     )
#
# print(
#     f"[13] - {TotalSongsPerDiff[3]} Songs\n"
#     f"{TotalFullCombos[3]} full combos\n"
#     "========================\n"
#     f"Total Fantastics: {TotalFantastics[3]}\n"
#     f"Total Excellents: {TotalExcellents[3]}\n"
#     f"Total Greats: {TotalGreats[3]}\n"
#     f"Total Decents: {TotalDecents[3]}\n"
#     f"Total Way Offs: {TotalWayOffs[3]}\n"
#     f"Total Misses: {TotalMisses[3]}\n"
#     )
        # if item[1][0] == 11:
        #     TotalFullCombos[1] += 1
        # elif item[1][0] == 12:
        #     TotalFullCombos[2] += 1
        # elif item[1][0] == 13:
        #     TotalFullCombos[3] += 1
    # for CurrentBlockDif in range(1, 15):
    #     if item[1][0] == 10 + CurrentBlockDif:
    #         pass

    # if item[1][0] == 11:
    #     TotalFantastics[1] += item[1][5]
    #     TotalExcellents[1] += item[1][6]
    #     TotalGreats[1] += item[1][7]
    #     TotalDecents[1] += item[1][8]
    #     TotalWayOffs[1] += item[1][9]
    #     TotalMisses[1] += item[1][10]
    #     TotalSongsPerDiff[1] += 1
    # elif item[1][0] == 12:
    #     TotalFantastics[2] += item[1][5]
    #     TotalExcellents[2] += item[1][6]
    #     TotalGreats[2] += item[1][7]
    #     TotalDecents[2] += item[1][8]
    #     TotalWayOffs[2] += item[1][9]
    #     TotalMisses[2] += item[1][10]
    #     TotalSongsPerDiff[2] += 1
    # elif item[1][0] == 13:
    #     TotalFantastics[3] += item[1][5]
    #     TotalExcellents[3] += item[1][6]
    #     TotalGreats[3] += item[1][7]
    #     TotalDecents[3] += item[1][8]
    #     TotalWayOffs[3] += item[1][9]
    #     TotalMisses[3] += item[1][10]
    #     TotalSongsPerDiff[3] += 1
