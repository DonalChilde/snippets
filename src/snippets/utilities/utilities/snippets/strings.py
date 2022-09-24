def stringInsert():
    line = "Kong Panda"
    index = line.find("Panda")
    output_line = line[:index] + "Fu " + line[index:]
    assert output_line == "Kong Fu Panda"
