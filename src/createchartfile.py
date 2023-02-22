def chart(track, sourceFile):
    # [Song]
    print("[Song]", file = sourceFile)
    print("{", file = sourceFile)
    print("  Name = \"" + track.name + "\"", file = sourceFile)
    print("  Artist = \"" + track.artist + "\"", file = sourceFile)
    print("  Charter = \"Richard Wills\"", file = sourceFile)
    print("  Album = \"" + track.album + "\"", file = sourceFile)
    print("  Year = \"" + track.year + "\"", file = sourceFile)
    print("  Offset = 0", file = sourceFile)
    print("  Resolution = 192", file = sourceFile)
    print("  Difficulty = 0", file = sourceFile)
    print("  PreviewStart = 0", file = sourceFile)
    print("  PreviewEnd = 0", file = sourceFile)
    print("  Genre = \"Unknown Genre\"", file = sourceFile)
    print("  MediaType = \"cd\"", file = sourceFile)
    print("  MusicStream = \"song.ogg\"", file = sourceFile)
    print("}", file = sourceFile)

    # [SyncTrack]
    print("[SyncTrack]", file = sourceFile)
    print("{", file = sourceFile)
    print("  0 = TS " + str(track.time_signature), file = sourceFile)
    print("  0 = B " + str(int(track.tempo * 1000)), file = sourceFile)
    
    for i in track.sections:
        print("  " + str(int(i * 1000)) + " = TS " + str(track.sections[i][1]), file = sourceFile)
        print("  " + str(int(i * 1000)) + " = B " + str(int(track.sections[i][0] * 1000)), file = sourceFile)

    print("}", file = sourceFile)

    # [Events]
    print("[Events]", file = sourceFile)
    print("{", file = sourceFile)
    print("}", file = sourceFile)

    # [Notes]
    print("[ExpertSingle]", file = sourceFile)
    print("{", file = sourceFile)
    in_use = {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    for time_stamp_s in sorted(track.frets.keys()):
        time_stamp_ms = int(time_stamp_s * 1000)
        for note in track.frets[time_stamp_s]:
            if time_stamp_ms >= in_use[0] and note[0] % 5 == 0:
                in_use[0] = time_stamp_ms + note[1]
                print("  " + str(time_stamp_ms) + " = N " + str(0) + " " + str(note[1]), file = sourceFile)
            elif time_stamp_ms >= in_use[1] and note[0] % 5 == 1:
                in_use[1] = time_stamp_ms + note[1]
                print("  " + str(time_stamp_ms) + " = N " + str(1) + " " + str(note[1]), file = sourceFile)
            elif time_stamp_ms >= in_use[2] and note[0] % 5 == 2:
                in_use[2] = time_stamp_ms + note[1]
                print("  " + str(time_stamp_ms) + " = N " + str(2) + " " + str(note[1]), file = sourceFile)
            elif time_stamp_ms >= in_use[3] and note[0] % 5 == 3:
                in_use[3] = time_stamp_ms + note[1]
                print("  " + str(time_stamp_ms) + " = N " + str(3) + " " + str(note[1]), file = sourceFile)
            elif time_stamp_ms >= in_use[4] and note[0] % 5 == 4:
                in_use[4] = time_stamp_ms + note[1]
                print("  " + str(time_stamp_ms) + " = N " + str(4) + " " + str(note[1]), file = sourceFile)
            else:
                continue

    print("}", file = sourceFile)