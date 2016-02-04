# deckbuilder-api
A tool to track your Hearthstone collection and decks.


## Users

#### Create a new user

**POST:**
```
/user
```

**Body:**
```json
{
  "username": "joe_user",
  "email": "user@example.com",
  "password": "password"
}
```

**Response:**
```json
{
  "id": 1,
  "email": "email@email.com",
  "username": "joe_user",
  "first_name": "",
  "last_name": "Name",
}
```

**Status Codes:**
* `201` if successful
* `400` if improper request

## Cards

### Get a list of Cards

**GET:** `/cards`

**Query Parameters:**

* `q`: search term
* `set`: if included filter on ['basic', 'classic', 'reward', 'naxx', 'gvg', 'brm, 'tgt', 'loe']

**Response:**
```json
{[
    {
        "id": 1124,
        "mana": 2,
        "name": "Wild Growth",
        "card_type": "spell"
    },
]}```

**Status Codes:**
* `200` if successful
* `400` if invalid query parameters

### Get a Card

**GET:** `/card/:id`

**Response:**
```json
{
    "id": 1124,
    "mana": 2,
    "name": "Wild Growth",
    "card_type": "spell"
}
```

**Status Codes:**
* `200` if successful
* `404` if does not exist

## Collection

### Get my collection

**GET:** `/collection/`

**Query Parameters:**

* query params

**Response:**
```json
{[
    {
        "id": 1124,
        "mana": 2,
        "name": "Wild Growth",
        "card_type": "spell",
        "count": 3
    },
]}
```

**Status Codes:**
* `200` if successful
* `400` if invalid query parameters
* `401` if invalid credentials

### Add/Remove a card to my collection

**PUT:** `/collection/[add|remove]`

**Body:**
```json
{
    "id": 1124,
    "count": 2
}
```

**Response:**
```json
{
    "id": 1124,
    "mana": 2,
    "name": "Wild Growth",
    "card_type": "spell",
    "count": 5
}
```

**Status Codes:**
* `200` if successful
* `400` if invalid data
* `401` if invalid credentials
* `404` if does not exist

## Decks

### Create Deck

**POST:** `/decks``

**Body:**
```json
{
    "name": "Midrange Druid",
    "hero": "druid",
    "cards": [
        {"1124": 2},

    ]
}
```

**Response:**
```json
{
    "name": "Midrange Druid",
    "hero": "druid",
    "cards": [
        {"1124": 2},
    ],
    "missing_cards": [],
    "mana_curve": [2,8,7,3,4,3,2,1]
}```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided
* `409` if unique constraint violation
