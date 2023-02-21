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

    for i in track.frets:
        for j in track.frets[i]:
            print("  " + str(int(i * 1000)) + " = N " + str(int(j[0] % 5)) + " " + str(j[1]), file = sourceFile)

    print("}", file = sourceFile)