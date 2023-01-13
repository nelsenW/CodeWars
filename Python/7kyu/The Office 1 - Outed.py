def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss]) / len(meet.values()) <= 5 else 'Nice Work Champ!'