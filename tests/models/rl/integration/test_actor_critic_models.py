import argparse

from pytorch_lightning import Trainer

from pl_bolts.models.rl.advantage_actor_critic_model import AdvantageActorCritic


def test_a2c():
    """Smoke test that the A2C model runs."""

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser = AdvantageActorCritic.add_model_specific_args(parent_parser)
    args_list = [
        "--env",
        "CartPole-v0",
    ]
    hparams = parent_parser.parse_args(args_list)

    trainer = Trainer(
        gpus=0,
        max_steps=100,
        max_epochs=100,  # Set this as the same as max steps to ensure that it doesn't stop early
        val_check_interval=1,  # This just needs 'some' value, does not effect training right now
        fast_dev_run=True,
    )
    model = AdvantageActorCritic(hparams.env)
    trainer.fit(model)
