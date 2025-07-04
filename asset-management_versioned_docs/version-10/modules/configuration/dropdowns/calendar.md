---
id: calendar
title: Calendar
---

# Calendar

The calendars used within i-Vertix ITAM are configurable by entity. They are
characterized by periods of opening as well as periods of closing.

These calendars are used in the `SLA`
(see Configure SLAs) and the
[configuration of entities](../../administration/entities).

## Calendar

### Time ranges

Corresponds to the opening time slots of the entity. You can add as many
as necessary per day as long as these slots do not overlap.

### Close times

Lists the closing periods assigned to this calendar and allows you to
add a new one; see
[lca configuration of closing periods](conf-close-periods).

### All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

## Close times 

The list of closure periods is a flat list of valid values. It can be
delegated by entity.

A closure period consists of a name, a period and whether this closure
is recurring or not.

Concerning the field Recurring, if it is in Yes it means that the period
indicated is valid all the time. In this case i-Vertix ITAM would not care about
the year indicated.

Very useful to indicate the holidays recurring each year (Christmas,
Victory of 1945, May 1 ...) or the period of closure of the company
(closed every year from 1 to 31 August) and especially it avoids
re-entering the same dates each year.
