"""
Security utilities for PII masking and sensitive data protection.
"""

import re
from typing import Dict, List, Tuple
from enum import Enum


class PiiType(Enum):
    """Types of personally identifiable information."""
    EMAIL = "email"
    PHONE = "phone"
    SSN = "ssn"
    CREDIT_CARD = "credit_card"
    IP_ADDRESS = "ip_address"


class PiiPatterns:
    """Patterns for detecting PII."""
    
    PATTERNS = {
        PiiType.EMAIL: r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        PiiType.PHONE: r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
        PiiType.SSN: r"\b\d{3}-\d{2}-\d{4}\b",
        PiiType.CREDIT_CARD: r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
        PiiType.IP_ADDRESS: r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    }


class SecurityManager:
    """Manages security operations like PII masking."""
    
    def __init__(self, enable_pii_masking: bool = True, enable_api_key_masking: bool = True):
        self.enable_pii_masking = enable_pii_masking
        self.enable_api_key_masking = enable_api_key_masking
        self.pii_replacements: Dict[PiiType, str] = {
            PiiType.EMAIL: "[EMAIL]",
            PiiType.PHONE: "[PHONE]",
            PiiType.SSN: "[SSN]",
            PiiType.CREDIT_CARD: "[CARD]",
            PiiType.IP_ADDRESS: "[IP]",
        }
    
    def mask_pii(self, text: str, pii_types: List[PiiType] = None) -> str:
        """
        Mask personally identifiable information in text.
        
        Args:
            text: Text to mask
            pii_types: List of PII types to mask. If None, masks all.
            
        Returns:
            Text with PII masked
        """
        if not self.enable_pii_masking:
            return text
        
        if pii_types is None:
            pii_types = list(PiiType)
        
        masked_text = text
        for pii_type in pii_types:
            pattern = PiiPatterns.PATTERNS.get(pii_type)
            if pattern:
                replacement = self.pii_replacements[pii_type]
                masked_text = re.sub(pattern, replacement, masked_text, flags=re.IGNORECASE)
        
        return masked_text
    
    def mask_api_key(self, api_key: str) -> str:
        """
        Mask API key for logging.
        
        Args:
            api_key: API key to mask
            
        Returns:
            Masked API key
        """
        if not self.enable_api_key_masking or not api_key or len(api_key) < 8:
            return "[MASKED]"
        
        visible_chars = 4
        return f"{api_key[:visible_chars]}...{api_key[-visible_chars:]}"
    
    def find_pii(self, text: str, pii_types: List[PiiType] = None) -> Dict[PiiType, List[str]]:
        """
        Find all PII in text.
        
        Args:
            text: Text to search
            pii_types: List of PII types to search for. If None, searches all.
            
        Returns:
            Dictionary mapping PII types to found instances
        """
        if pii_types is None:
            pii_types = list(PiiType)
        
        found_pii: Dict[PiiType, List[str]] = {}
        
        for pii_type in pii_types:
            pattern = PiiPatterns.PATTERNS.get(pii_type)
            if pattern:
                matches = re.findall(pattern, text, flags=re.IGNORECASE)
                if matches:
                    found_pii[pii_type] = matches
        
        return found_pii
    
    def sanitize_log(self, log_data: Dict) -> Dict:
        """
        Sanitize log data by masking sensitive information.
        
        Args:
            log_data: Log data dictionary
            
        Returns:
            Sanitized log data
        """
        sanitized = {}
        
        sensitive_keys = {"password", "token", "key", "secret", "api_key", "credentials"}
        
        for key, value in log_data.items():
            if any(sensitive in key.lower() for sensitive in sensitive_keys):
                if isinstance(value, str):
                    sanitized[key] = self.mask_api_key(value)
                else:
                    sanitized[key] = "[MASKED]"
            elif isinstance(value, str):
                sanitized[key] = self.mask_pii(value)
            elif isinstance(value, dict):
                sanitized[key] = self.sanitize_log(value)
            elif isinstance(value, list):
                sanitized[key] = [
                    self.sanitize_log(item) if isinstance(item, dict) else
                    self.mask_pii(item) if isinstance(item, str) else
                    item
                    for item in value
                ]
            else:
                sanitized[key] = value
        
        return sanitized
