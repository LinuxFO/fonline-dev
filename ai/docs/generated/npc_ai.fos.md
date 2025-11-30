---
title: npc_ai.fos
description: " FOnline: 2238 Rotators  npc_ai.fos ..."
---

# npc_ai.fos


FOnline: 2238
Rotators

npc_ai.fos


## Includes

- `_ai.fos`
- `_defines.fos`
- `ITEMPID.H`

## Included By

- [cheats.fos](cheats.fos.md)
- [combat.fos](combat.fos.md)
- [main_planes.fos](main_planes.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| AI_AGGRESSION | `# (ai)         AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 0)]` | AI data offsets |
| AI_MAX_DIST | `# (ai)           AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 1)]` |  |
| AI_MIN_HP | `# (ai)             AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 2)]` |  |
| AI_MIN_TO_HIT | `# (ai)         AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 3)]` |  |
| AI_CAN_OPEN_DOORS | `# (ai)     (AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 4)] != 0)` |  |
| AI_ATTACK_AREA | `# (ai)        AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 5)]` |  |
| AI_ATTACK_WHO | `# (ai)         AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 6)]` |  |
| AI_BEST_WEAPON | `# (ai)        AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 7)]` |  |
| AI_CHEM_USE | `# (ai)           AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 8)]` |  |
| AI_DISPOSITION | `# (ai)        AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 9)]` |  |
| AI_DISTANCE | `# (ai)           AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 10)]` |  |
| AI_HURT_TO_MUCH_0 | `# (ai)     AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 11)]` |  |
| AI_HURT_TO_MUCH_1 | `# (ai)     AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 12)]` |  |
| AI_RUN_AWAY | `# (ai)           AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 13)]` |  |
| AI_CALLED_FREQ | `# (ai)        AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 14)]` |  |
| AI_SECONDARY_FREQ | `# (ai)     AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 15)]` |  |
| AI_MESS_CHANCE | `# (ai)        AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 16)]` |  |
| AI_GENERAL_TYPE | `# (ai)       AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 17)]` |  |
| AI_BODY_TYPE | `# (ai)          AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 18)]` |  |
| AI_CHEM_PRIM_DESIRE_0 | `# (ai) AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 19)]` |  |
| AI_CHEM_PRIM_DESIRE_1 | `# (ai) AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 20)]` |  |
| AI_CHEM_PRIM_DESIRE_2 | `# (ai) AIData_[(((ai) < AIPACKET_COUNT ? (ai) : 0) * 22 + 21)]` |  |

## Functions

### AI_TrySayCombatText

```angelscript
void AI_TrySayCombatText(Critter& npc, int textType)
```

### AI_TrySayCombatText

```angelscript
void AI_TrySayCombatText(Critter& npc, int textType, bool force)
```


