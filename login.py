import sys
import os
from ZAminofix import Client

def login_with_sid(sid: str) -> Client:
    try:
        # Create a new client instance
        client = Client()
        
        # Login using SID
        client.login_sid(SID=sid)
        
        # Verify login was successful
        if client.authenticated:
            print(f"✅ Successfully logged in!")
            print(f"👤 User ID: {client.userId}")
            print(f"🔑 SID: {client.sid[:20]}...")
            return client
        else:
            raise Exception("Authentication failed - client not authenticated")
            
    except Exception as e:
        print(f"❌ Login failed: {str(e)}")
        raise

def main():
    """Main function to handle command line usage"""
    if len(sys.argv) > 1:
        # Get SID from command line argument
        sid = sys.argv[1]
    else:
        # Interactive mode - prompt user for SID
        print("🔐 Amino SID Login")
        print("=" * 40)
        sid = input("Enter your SID: ").strip()
    
    if not sid:
        print("❌ Error: SID cannot be empty")
        sys.exit(1)
    
    try:
        # Attempt login
        client = login_with_sid(sid)
        
        # Show additional info
        print("\n📋 Account Info:")
        print(f"   Nickname: {getattr(client.account, 'nickname', 'N/A')}")
        print(f"   Amino+ Status: {'Active' if hasattr(client.account, 'membership') else 'Inactive'}")
        
        return client
        
    except Exception as e:
        print(f"❌ Failed to login: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
