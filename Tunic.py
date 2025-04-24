# Fake "instruction manual" page generator
def generate_manual_page():
    icons = ["⚔️", "🛡️", "❤️", "🔑"]
    return f"""
    {random.choice(icons)} Press [A] to attack
    {random.choice(icons)} [B] opens inventory
    {random.choice(icons)} ??? symbols mean danger
    """
