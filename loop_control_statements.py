jungle = ["tiger", "snake", "bear", "gorilla", "exit"]
for animal in jungle:
   if animal == "exit":
      print("You've reached the exit. Safe now!")
      break
   elif animal == "gorilla":
      print("A gorilla appeared! Stay calm and be quiet.")
      continue
   print("Encountered", animal, "- Be careful!")