# List of possible on-actions

Try to keep this reasonably up-to-date, please.

(updated 2026-05)

### General
- `on_startup`
- `on_daily`
- `on_daily_TAG`
- `on_weekly`
- `on_weekly_TAG`
- `on_monthly`
- `on_monthly_TAG`
- `on_nuke_drop`
- `on_pride_of_the_fleet_sunk`
- `on_naval_invasion`
- `on_paradrop`

### Politics
- `on_stage_coup`                       - ROOT is the country that stages the coup, FROM is the target country  
- `on_coup_succeeded`
- `on_government_change`
- `on_ruling_party_change`
- `on_ruling_party_change_immediate`    - [deprecated] Unsafe behavior, prefer using on_ruling_party_change instead
- `on_new_term_election`
- `on_before_peace_conference_start`    - ROOT is winner, FROM is loser (called for all winners against all losers)
- `on_peaceconference_started`          - ROOT is winner, FROM is loser (called for all winners against all losers)
- `on_peaceconference_ended`            - ROOT is winner, FROM is loser (called for all winners against all losers)

### Diplomacy/War
- `on_send_volunteers`
- `on_recall_volunteers`
- `on_border_war_lost`
- `on_war_relation_added`
- `on_declare_war`
- `on_war`
- `on_peace`
- `on_capitulation`
- `on_capitulation_immediate`
- `on_uncapitulation`
- `on_annex`
- `on_civil_war_end_before_annexation`
- `on_civil_war_end`
- `on_puppet`
- `on_force_government`
- `on_liberate`
- `on_release_as_free`
- `on_release_as_puppet`
- `on_guarantee`                        - 	ROOT is the country which guarantees, FROM is the country that is guaranteed.
- `on_military_access`                  - 	ROOT is the country which requested, FROM is the country that accepted.
- `on_offer_military_access`            -   ROOT is the country which offered, FROM is the country that accepted.
- `on_call_allies`
- `on_join_allies`
- `on_lend_lease`
- `on_incoming_lend_lease`
- `on_send_expeditionary_force`
- `on_return_expeditionary_forces`
- `on_request_expeditionary_forces`
- `on_peace_proposal`
- `on_send_attache`

### Faction
- `on_create_faction`
- `on_faction_formed`
- `on_offer_join_faction`
- `on_join_faction`
- `on_assume_faction_leadership`
- `on_leave_faction`

### Autonomy
- `on_subject_annexed`
- `on_subject_free`
- `on_subject_autonomy_level_change`

### Governments In Exile
- `on_government_exiled`
- `on_host_changed_from_capitulation`
- `on_exile_government_reinstated`

### States
- `on_state_control_changed`

### Wargoals
- `on_generate_wargoal`                 -   ROOT is the wargoal owner, FROM is the wargoal target
- `on_justifying_wargoal_pulse`
- `on_wargoal_expire`

### Unit Leader
- `on_unit_leader_created`
- `on_army_leader_daily`
- `on_army_leader_won_combat`
- `on_army_leader_lost_combat`
- `on_unit_leader_level_up`
- `on_army_leader_promoted`
- `on_deployed_leader_defeated`

### Aces
- `on_ace_promoted`
- `on_ace_killed`
- `on_ace_killed_on_accident`
- `on_non_ace_killed_other_ace`
- `on_ace_killed_by_ace`
- `on_ace_killed_other_ace`
- `on_aces_killed_each_other`

### La Resistance
- `on_operation_completed`
- `on_operative_detected_during_operation`
- `on_operative_on_mission_spotted`
- `on_operative_captured`
- `on_operative_created`
- `on_operative_death`
- `on_operative_recruited`
- `on_fully_decrypted_cipher`
- `on_activated_active_decryption_bonuses`

### MIO
- `on_mio_size_increased`
- `on_mio_design_team_assigned_to_tech`
- `on_mio_design_team_assigned_to_variant`
- `on_mio_industrial_manufacturer_assigned`
- `on_mio_tech_reseach_cancelled`
- `on_mio_tech_reseach_completed`
- `on_mio_industrial_manufacturer_unassigned`
