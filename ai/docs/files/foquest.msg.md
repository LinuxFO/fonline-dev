# FOQUEST.MSG

## Brave New World (BNW) update by Sasa

FOClassic tutorials and Brave New World update can be found at:

<https://fodev.net/forum/index.php/topic,30344.msg263172.html#msg263172>

Quest Tabs (101):

- Should prefix location if that is known before every quest. Pip-boy will sort alphabetically, thus quest group will form naturally.

Quest Info (102):

- Following keywords can be added to be processed by Quest Tracker (note that `':'` is part of the keyword).
- `'JOB:'` denotes a repeatable task. If the task is completed or failed, it can be attempted at a later time.
- `'STORY:'` denotes important or main story lines, for example Vault 24 quest.
- `'QUEST:'` denotes everything else, it can be ommited and Quest Tracker will default to this, but I have added it for clarity.

Quest Progress (1-100):

- Following keywords can be added to be processed by Quest Tracker (note that `':'` is part of the keyword).
- `'HIDDEN:'` progress will not appear in Pip-boy or Quest Tracker. (used if code cycles through values that do not have entry, otherwise Pip-boy would show 'error' as description).
- `'NO_POPUP:'` progress will not appear in Pip-boy or Quest Tracker. (to suppress some quest changes, if they would pop up too offten, ex: while in dialog mode fast progressing quests).
- `'DONE:'` quest` is ready, player can go back to quest giver to get rewards. (ex: kill dogs quest, show player all dogs are dead and they can leave are).
- `'SOFT_FAILED:'` quest failed but can be attempted again at a later time.
- `'HARD_FAILED:'` quest failed for good and cannot be attempted later.
- `'SOFT_COMPLETED:'` quest completed and can be re-taken at a later time. (ex: JOB: type of tasks/quests).
- `'HARD_COMPLETED:'` quest completed for good.
- `'ONGOING:'` default behaviour, no extra coloring in Quest Tracker.

Numbering convention to follow when making new quests:

- `000:` DO NOT USE - This is reserved for when quest is not in pip-boy.
- `001-009:` Billboards/Gossip - Character received info about possible quest from billboards or gossip, when refactoring check var agains `'< 10'`, rather than `'== 0'`.
- `010:` Unused - When refactoring, just add 10 to the progress numbers, 0 -> 10, hence this should not be used as 0 means not in pip-boy.
- `011-069:` Actual Progress - Quest progress describing what actions were taken or what is next step/objective of quest.
- `070-079`: Done, report back - Quest objective has been finished, player only need to go back to notify NPC.
- `080:` Repeatable Job available again - Job reclaimed by garbager should set this value, use 'NO_POPUP:'. When checking against repeatable status only need to do a `[q_var] >= 80` in dialog demands.
- `081-089:` Failed/Soft Failed - Describe cause of failure and if retakeable later.
- `090-099:` Completed/Soft Completed - Describe finished state and if retakeable later.
- `100:` Unused - Not sure how engine handles this, just avoid.

Note: I didn't refactor everything to use this yet, but seems to be the best convention.
