# Groq API Key Setup Guide

## Getting a Valid API Key

1. **Visit Groq Console**: Go to [console.groq.com](https://console.groq.com)
2. **Sign In/Sign Up**: Use your email or create a new account
3. **Navigate to API Keys**: 
   - Click on "API Keys" in the left sidebar
   - Or go to [console.groq.com/keys](https://console.groq.com/keys)
4. **Create New Key**:
   - Click "Create Key"
   - Give it a name (e.g., "AI Code Assistant")
   - Copy the key immediately (it won't be shown again)

## Valid API Key Format
A valid Groq API key should start with `gsk_` and be about 40+ characters long:
```
gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Updating Your API Key

Once you have a valid key, update it in these locations:

### 1. Environment Variable
```bash
export GROQ_API_KEY="your_new_valid_key_here"
```

### 2. Streamlit Secrets
Update `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_new_valid_key_here"
```

### 3. Application Code
Update the hardcoded key in `main.py` if present.

## Troubleshooting

- **Organization Restricted**: This means the key is invalid or has restrictions
- **Invalid Request**: Check the key format and ensure it's not expired
- **Rate Limited**: You may have exceeded usage limits

## Getting Help
If you continue to have issues:
- Contact Groq support at [support@groq.com](mailto:support@groq.com)
- Check the Groq documentation at [docs.groq.com](https://docs.groq.com)
