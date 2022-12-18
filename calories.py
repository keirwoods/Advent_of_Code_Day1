elves = [1000, 2000, 3000, None, 4000, None, 5000, 6000, None, 7000, 8000, 9000, None, 10000]
elf_count = 0
packagecalories = 0
calories = 0
for elf, package in enumerate(elves):
  if isinstance(package,__builtins__.int):
    packagecalories = packagecalories + package
  elif package == None:
    elf_count = elf_count +1
    print(packagecalories) 
    if packagecalories > calories:
      calories = packagecalories
      whichelf = elf_count
    packagecalories = 0
print(f"found this many elves {elf_count}")
print(f"elf with most calories is {whichelf} with {calories} calories")