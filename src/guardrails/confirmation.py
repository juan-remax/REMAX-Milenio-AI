CRITICAL_ACTIONS = [
    "enviar mensaje a cliente",
    "publicar en portal",
    "modificar precio",
    "eliminar propiedad",
    "crear issue en github",
]


def is_critical_action(action: str) -> bool:
    return any(keyword in action.lower() for keyword in CRITICAL_ACTIONS)


def needs_confirmation(action: str) -> bool:
    return is_critical_action(action)
