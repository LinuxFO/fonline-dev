---
title: prod_ingredients.fos
description: " FOnline: 2238 Rotators  prod_ingredients.fos ..."
---

# prod_ingredients.fos


FOnline: 2238
Rotators

prod_ingredients.fos


## Includes

- `_defines.fos`
- `prod_ingredients_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __PROD_INGREDIENTS__ |  |  |

## Functions

### HaveAnyIngredient

```angelscript
bool HaveAnyIngredient(Item& item)
```

### HaveIngredient

```angelscript
bool HaveIngredient(Item& item, uint8 ingredient)
```

### GetIngredientReturnItem

can be zero!

```angelscript
uint16 GetIngredientReturnItem(Item& item, uint8 ingredient)
```

### IngredientName

```angelscript
string IngredientName(uint8 ingredient)
```

### IngredientsNames

```angelscript
uint IngredientsNames(Item& item, array<string>& names)
```


