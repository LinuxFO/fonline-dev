# Special NPCs

There is a few NPCs (or rather dialogs) of special purpose which you might find useful at some point (for example to make events or for testing).

```text
`addnpc 170 -d 10799 -l 9999
```

Low tech outfitter.

```text
`addnpc 486 -d 10809 -l 9999
```

High tech outfitter.

```text
`addnpc 278 -d 10802 -l 9999
```

Altruist (gives free XP and money).

```text
`addnpc 251 -s vaul_guard@critter_init -l 9999 -r 1 -b 191
```

Event Enclave guard with sniper rifle.

```text
`addnpc 454 -d 2530 -s npc_shouter@critter_init -role 5 -a 238 -b 1 -t 9000
```

Hub Arena shouter. He shouts that a fighting event in the Hub Arena is taking place. Talking to him gives the option to teleport directly into the arena. (Was meant to be placed on every corner in the Hub when fight events are taking place).

Finally there is a special command to make a teleporter NPC:

```text
`teleporter -map mapId -tx targetHexX -ty targetHexY [-x hexX] [-y hexY] [-dir direction] [-it]
```

Teleporter Goris. Will teleport players to a map at specified coordinates. Use `-it` flag to allow teleportation with items.
