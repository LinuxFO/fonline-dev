# Item/Location legitimacy system

Every item and map in the game is either legit or not legit. All items and locations created by standard game features are considered legit.

Items spawned with GM commands, are not legit, unless you use `-legit` switch in the commands. The switch can be used only with admin access level, in following commands:

```text
createlocation
give
givekey
spawncar
spawnitem
```

In case of items, the `-legit` switch should be used ONLY when you spawn an item which is supposed to be 100% legal part of the game, used by all players however they want. The same goes for locations.

## Legit item behavior

Spawned legit items and locations behave like any other legit item and location in the game.

## Not legit item behavior

Spawned not legit items can be used by authenticated staff (tester access and higher) anywhere without most restrictions . By non-authenticated players they can be used without restrictions only inside not legit locations. There is a small exception for stackable items. Even in not legit location, stackable not legit items can't be picked up or used if player holds a legit item of the same kind (to prevent merging not legit stacks into legit stacks).

Not legit items can't be disassembled (not even in not legit locations).

You should still take all possible precautions when spawning items (the system helps prevent the most common mistakes, but it's far from perfect and there are many loopholes in it).
