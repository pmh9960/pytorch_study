import wandb

if __name__ == "__main__":
    wandb.init(name="first-model", project="first-wandb", entity="mpark")
    wandb.finish()
    # 등등 사용할 수 있다... 나중에 따로 하나하나 기능 쓰면서 알아보기
