from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Boto3Config(BaseSettings):
    service_name: str = "s3"
    key_id: str = Field(alias="R2_ACCESS_KEY_ID")
    access_key: str = Field(alias="R2_SECRET_ACCESS_KEY")
    bucket_name: str = "outerspy-bucket"
    account_id: str = Field(alias="R2_ACCOUNT_ID")

    @property
    def endpoint_url(self):
        return f"https://{self.account_id}.r2.cloudflarestorage.com"


boto3_config = Boto3Config()
