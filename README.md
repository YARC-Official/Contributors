# Contributors
This is a repository containing a list of contributors for YARC projects (YARG, OpenSource, etc.), with social links.

**If you contributed to any YARC projects ([listed below](#contributions)), please feel from to open a PR to have your credit shown! Your contribution matters, big or small.** Feel free to also open an issue with your info, and I'll add it for you.

# 📝 Specifications

Here is an example entry. More possible keys and values are shown below.

```json
{
    "Name": "EliteAsian",
    "SpecialRole": "Founder",
    "Socials": {
        "Twitter": "EliteAsian123",
        "Twitch": "eliteasian123",
        "Github": "EliteAsian123",
        "VideoService": "UC0k5Wnt4vdbbb7ht_74I-Dg",
        "Discord": "eliteasian",
        "Email": "eliteasian123@gmail.com",
        "Website": "https://eliteasian123.github.io"
    },
    "Contributions": {
        "OpenSource": [ "Developer" ],
        "YARC-Charters": [ "Charter" ],
        "YARC-Launcher": [ "Developer" ],
        "YARG": [ "Developer", "Artist" ]
    }
}
```

## `contributors.json`

A `Contributor[]`. This list is not sorted, and new entries should just be added at the bottom.

## `Contributor`

| Key | Description | Data type / Possible values |
| --- | --- | --- |
| `Name` | The display name of the contributor. | `string` |
| `SpecialRole` | A contributor's special role (such as a leadership role). **This can only be given by EliteAsian**. | `string` |
| `Socials` | The contributor's social media accounts **that will be shown publicly**. | `Socials` |
| `Contributions` | The projects that the contributor has contributed to, and how they contributed to them. | `Contributions` |

## `Socials`

| Key | Description | Data type / Possible values                                                     |
| --- | --- |---------------------------------------------------------------------------------|
| `Twitter` | Twitter/X | A user's Twitter handle without the `@`.                                        |
| `Bluesky` | Bluesky | A user's Bluesky username. (`.bsky.social` will be appended if there is no dot) |
| `Twitch` | Twitch | A user's Twitch username.                                                       |
| `Github` | GitHub | A user's GitHub username.                                                       |
| `VideoService` | Any video service (because copyright), such as YouTube. | Any URL, YouTube ID, or YouTube username (with the `@`).                        |
| `Discord` | Discord | A user's Discord username.                                                      |
| `Email` | Any email address. | A valid email address. **This will be public.**                                 |
| `Website` | The contributor's personal website. Only valid address are allowed. | Any URL.                                                                        |

## `Contributions`

Any key that corresponds to a GitHub repository or a special team name. Currently accepted list:
* `OpenSource`
* `YARC-Charters`
* `YARC-Launcher`
* `YARG`
* `Community`

The value is a `string[]`, where each element must be one of the following:
* `Developer`
* `Artist`
* `Charter`
* `Moderator`
* `SFXArtist`
* `QATester`
* `DocContributor`
* `Localizer`
