# Country Decisions

Decisions are made available to countries that fulfill the right conditions.
Some triggers are only checked once per day, once per frame or once per game.

`allowed`:
- Scope: THIS = Country
- Checked once per game at start (or when save is loaded)
- Used to filter out decisions that will never be available to a given country (usually checks `original_tag = XXX`)
- Important to use on performance-heavy decisions (especially targeted decisions) to avoid unnecessary computations

`visible`:
- Scope: THIS = Country, FROM = Country/State (if targeted)
- Checked each frame when the interface is refreshed if allowed was true
- Used to filter out decisions that should appear in decision interface (they may still be greyed out, see `available` next)
- Caveat: this trigger can become performance heavy for targeted decisions, see `target_root_trigger` and `target_trigger`.

`available`:
- Scope: THIS = Country, FROM = Country/State (if targeted)
- Checked each frame when the interface is refreshed if both allowed and visible were true
- Used to indicate if a visible decision can be taken right now and it not, what the player should do to be able to.
  No condition should be impossible to match at this point (for example, do not require completion of locked out focus)

`target_root_trigger`:
- Scope: THIS = Country
- Checked once per day (updated in one of the 24 hourly ticks depending on country), if allowed was true
- Used to lessen the impact of targeted decisions that cannot be restricted by `targets` and `allowed`.
  Since targeted decisions are checked against each state/country in the game each frame in the `visible` trigger, this offers a way to do a pre-check once a day.
  This trigger should be a subset of the `visible` trigger that only uses the acting country scope.

`target_trigger`:
- Scope: THIS = Country, FROM = Target Country/State
- Checked once per day for each state/country in the world if both allowed and `target_root_trigger` were true.
- Used to select which country/states this targeted decision should apply to. Each match will create a dedicated decision entry.
- Similarly to `target_root_trigger`, this should contain a subset of the `visible` trigger that pertains to a given target state/country.
  The lower frequency of this check will help avoiding checking the visible trigger against each country/state each frame when possible.

`state_trigger`:
 - Possible values: `yes`, `no`, `any`, `any_owned_state`, `any_controlled_state`, `continent_key` (`europe`, `africa`, `north_america`...)
 - This will only have an effect if no `targets` are specified, else this should be set to `any` (or `yes`) if targets are used.
 - Unless omitted or set to `no`, makes the decision a state targeted decision. Which states will be checked depends on value:
    - `any` (or `yes`): will check every state in the game against the `target_trigger`. To be avoided whenever possible as this is expensive performance wise.
    - `any_owned_state`: will check every state owned by the country. This is equivalent (but quite faster) to adding `owner = ROOT` in the target_trigger.
    - `any_controlled_state`: will check every state controlled by the country. This is equivalent (but quite faster) to adding `is_controlled_by = ROOT` in the `target_trigger`.
    - `continent_key` (`europe`, `africa`, `north_america`...): will check every state in the continent. This is equivalent (but quite faster) to adding `is_on_continent = xxx` in the `target_trigger`.
