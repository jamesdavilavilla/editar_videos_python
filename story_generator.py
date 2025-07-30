import random
def generate_stories(n=1):
    prompts = [
        "Mi novia desapareció por 2 días y volvió como si nada...",
        "Encontré una carta escondida en la chaqueta de mi papá...",
        "Mi mejor amigo me traicionó y ahora vive con mi ex...",
        "Soñé algo extraño... y al día siguiente sucedió en la vida real.",
    ]
    stories = []
    for _ in range(n):
        base = random.choice(prompts)
        parts = [base] + [f"Parte {i+1}: ..." for i in range(5)]
        stories.append(parts)
    return stories
