# FOnline: 2238 GM Abuse Tutorial

This thread is made to answer some basic questions about administrating/game mastering a FOnline: 2238 server from inside the game (commonly known as abusing). It's assumed you already know hardcoded FOnline SDK commands and the basics about FOnline server.

Note: in the following posts the "admin" term will usually mean a person with any access level higher than player. A term "access level" will be used whenever there will be a need to make a clear distinction between different access levels of admins (tester, moder or admin).

Let's get started!

## Configuring admin access: GetAccess.cfg

Before your team can start to abuse the server you have to define access settings. To do this, create a file GetAccess.cfg inside the FOnline: 2238 Server/config/ subfolder. The file should contain a list of all admins, each with own unique password and an appropriate access level. A small example how such setting for a single admin should look like inside the file:

```ini
[AdminName]
Access=admin
Password=myuniquepassword
```

There are three possible access levels (from the lowest to the highest): tester, moder, admin.

It is important for passwords to be unique for every admin. Although not necessary, it is advised for AdminName to be the same as the name of the character account the admin wants to use for administrative / game mastering purposes. If the character account can't be created right away, it is possible to prevent registration of a character with AdminName name by adding a line `Reserved=true`. It can be useful for example if you wipe a server and not all GMs are around to make an account right away. Later you can remove the blockade with command `accesslist allowregistration AdminName or simply by editing GetAccess.cfg file (however this requires server restart).

Note: The Ids of all character accounts the admin uses with `~getaccess` are written automatically in GetAccess.cfg. This way you can check if someone isn't using admin access on characters they aren't supposed to.

## GodOfTheRealm

There is a special admin mode scripted in FOnline: 2238 - GodOfTheRealm. Characters with this mode will be invisible for everyone else (even other people with GodOfTheRealm) and have stronger protection against being abused by other admins. This mode is given by editing return value of bool GodOfTheRealm function in the cheats.fos module. After it's done, the admin can run god function from the cheats.fos module to become GodOfTheRealm. To go back to normal mode the admin can run mortal function.

## AdminLook

There is an adminlook function in cheats.fos module which can be run by people with admin access level. The function grants perfect sneaking (being able to sneak from everyone except admins) and perfect vision (seeing everyone in map except GodOfTheRealm characters). It can be also used on other characters if you know a secret number passed as the second argument of the function - use it to give adminlook to people with tester and moder access levels. Before you start your server you should change this number.

## Getting Access

Getting tester/moder/admin access level works the same way as in FOnline SDK - use `~getaccess (client | tester | moder | admin) password` command. The only difference is, the password is defined in GetAccess.cfg file instead of the server config file. After you type the right password you are ready to use Game Master Tools (if you set it up in the client, see the post below) and server commands!
