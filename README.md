# deckbuilder-api
A tool to track your Hearthstone collection and decks.


## API Documentation

### Index
1. [Create a new user](#create-a-new-user)
1. [Get a list of Cards](#get-a-list-of-cards)
1. [Get a Card's details](#get-a-cards-details)
1. [Get Collection](#get-collection)
1. [Add a Card to Collection](#add-a-card-to-collection)
1. [Remove a Card from Collection](#remove-a-card-from-collection)
1. [Create a Deck](#create-a-deck)
1. [Get a list of Decks](#get-a-list-of-decks)
1. [Get details of a Deck](#get-details-of-a-deck)
1. [Update a Deck](#update-a-deck)
1. [Delete a Deck](#delete-a-deck)


### Users

#### Create a new user

**POST:** `/user`

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
    "last_name": ""
}
```

**Status Codes:**
* `201` if successful
* `400` if invalid data


### Cards

#### Get a list of Cards

**GET:** `/card`

**Query Parameters:**
- `q`: search term
- `set`: if included filter on `basic`, `classic`, `reward`, `naxx`, `gvg`, `brm, `tgt`, `loe`

**Response:**
```json
{
    "count": 741,
    "next": "http://testserver/card/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Mind Control",
            "mana": 10,
            "hero": "priest",
            "card_type": "spell",
            "card_set": "basic",
            "rarity": "common",
            "text": "Take control of an enemy minion.",
            "tribe": null,
            "attack": null,
            "health": null
        },
        {
            "id": 2,
            "name": "Prophet Velen",
            "mana": 7,
            "hero": "priest",
            "card_type": "minion",
            "card_set": "classic",
            "rarity": "legendary",
            "text": "Double the damage and healing of your spells and Hero Power.",
            "tribe": null,
            "attack": 7,
            "health": 7
        },
        ...
    ]
}
```

**Status Codes:**
* `200` if successful
* `400` if invalid query parameters


#### Get a Card's details

**GET:** `/card/:id`

**Response:**
```json
{
    "health": null,
    "mana": 10,
    "attack": null,
    "card_type": "spell",
    "rarity": "common",
    "text": "Take control of an enemy minion.",
    "card_set": "basic",
    "hero": "priest",
    "id": 1,
    "name": "Mind Control",
    "tribe": null
}
```

**Status Codes:**
* `200` if successful
* `404` if does not exist


## Collection

#### Get Collection

**GET:** `/collection`

**Query Parameters:**
- query params for filtering

**Response:**
```json
[
    {
        "id": 1124,
        "mana": 2,
        "name": "Wild Growth",
        "card_type": "spell",
        "count": 3
    },
    {
        "id": 400,
        "mana": 1,
        "name": "Arcane Missles",
        "card_type": "spell",
        "count": 2
    },
]
```

**Status Codes:**
* `200` if successful
* `400` if invalid query parameters
* `401` if invalid credentials


#### Add a Card to Collection

**PUT:** `/collection/add`

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
* `404` if `id` does not exist


#### Remove a Card from Collection

**PUT:** `/collection/remove`

**Body:**
```json
{
    "id": 400,
    "count": 1
}
```

**Response:**
```json
{
    "id": 400,
    "mana": 1,
    "name": "Arcane Missles",
    "card_type": "spell",
    "count": 1
}
```

**Status Codes:**
* `200` if successful
* `400` if invalid data
* `401` if invalid credentials
* `404` if `id` does not exist


### Decks

#### Create a Deck

**POST:** `/deck`

**Body:**
```json
{
    "name": "Midrange Druid",
    "hero": "druid",
    "cards": [
        {"id": 1124, "count": 2},
        ...
    ]
}
```

**Response:**
```json
{
    "id": 7,
    "name": "Midrange Druid",
    "hero": "druid",
    "cards": [
        {"id": 1124, "count": 2},
        ...
    ],
    "missing_cards": [],
    "mana_curve": [2, 8, 7, 3, 4, 3, 2, 1]
}```

**Status Codes:**
- `201` if successful
- `400` if incorrect data provided
- `409` if unique constraint violation


#### Get a list of Decks

**GET:** `/deck`

**Body:** None

**Response:**
```json
[
    {
        "name": "Midrange Druid",
        "hero": "druid",
        "cards": [
            {"id": 1124, "count": 2},
            ...
        ],
        "missing_cards": [],
        "mana_curve": [2, 8, 7, 3, 4, 3, 2, 1]
    },
    {
        "name": "Aggro Warrior",
        "hero": "warrior",
        "cards": [
            {"id": 365, "count": 2},
            {"id": 447, "count": 1},
            ...
        ],
        "missing_cards": [],
        "mana_curve": [0, 3, 7, 6, 6, 4, 2, 2]
    }
]
```

**Status Codes:**
- `200` if successful


#### Get details of a Deck

**GET:** `/deck/:id`

**Body:** None

**Response:**
```json
{
    "name": "Midrange Druid",
    "hero": "druid",
    "cards": [
        {
            "id": 1124,
            "mana": 2,
            "name": "Wild Growth",
            "card_type": "spell",
            "class": "druid",
            "count": 2
        }
    ],
    "missing_cards": [],
    "mana_curve": [2, 8, 7, 3, 4, 3, 2, 1]
}
```

**Status Codes:**
- `201` if successful
- `400` if incorrect data provided
- `409` if unique constraint violation


#### Update a Deck

**PATCH:** `/deck/:id`

**Body:** 
```json
{
    "name": "Aggro Druid"
}

**Notes:**
The following fields can be edited:
- `name`
- `cards`

**Response:**
```json
{
    "name": "Aggro Druid",
    "hero": "druid",
    "cards": [
        {
            "id": 1124,
            "mana": 2,
            "name": "Wild Growth",
            "card_type": "spell",
            "class": "druid",
            "count": 2
        },
        ...
    ],
    "missing_cards": [],
    "mana_curve": [2, 8, 7, 3, 4, 3, 2, 1]
}
```

**Status Codes:**
- `200` if successful
- `400` if incorrect data provided
- `401` if invalid or missing auth
- `404` if deck is not found
- `409` if unique constraint violation


#### Delete a Deck

**DELETE:** `/deck/:id`

**Body:** None

**Response:** None

**Status Codes:**
- `204` if successful
- `404` if deck not found

