import bcrypt

# models
from clientboards.api.models import Users


def hashPassword(string: str) -> str:
    """
    Hashes a string using bcrypt
    """
    hashedPassword = bcrypt.hashpw(string.encode(
        'utf-8'), bcrypt.gensalt()).decode('utf-8')
    return hashedPassword


def verifyPasswordHash(string: str, email: str) -> bool:
    """
    Verifies that a string matches the hashed password in the database for a given email
    """
    try:
        user = Users.objects.get(email=email)
        hashedPassword = user.password
        return bcrypt.checkpw(string.encode('utf-8'), hashedPassword.encode('utf-8'))
    except Exception:
        return False
