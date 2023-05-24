"""Service functions."""
from pathlib import Path

import neurots
import pylab as plt
import tmd.io
import tmd.view

from app import utils

# pylint: disable=unused-argument


def make_synthesis_inputs(
    parameters_file: Path,
    distributions_file: Path,
    total_extent: float,
    randomness: float,
    orientation: tuple[float, float, float],
    step_size: float,
    radius: float,
):
    """Generate and update the synthesis inputs."""
    parameters = utils.load_json(parameters_file)
    # _modify_parameters(parameters, randomness, orientation, step_size, radius)

    distributions = utils.load_json(distributions_file)
    # _modify_distributions(distributions, total_extent)

    return parameters, distributions


def synthesize_morphology(parameters, distributions):
    """Grow a morphology using the parameters and distributions."""
    grower = neurots.NeuronGrower(parameters, distributions)
    grower.grow()

    return tmd.io.load_neuron_from_morphio(grower.neuron.as_immutable())


def make_figure(morphology) -> plt.Figure:
    """Make an analysis figure."""
    barcode = tmd.methods.get_ph_neuron(morphology, neurite_type="dendrites")

    fig = plt.figure()

    # ruff: noqa: F841
    # pylint: disable=unused-variable

    ax1 = fig.add_subplot(321)
    tmd.view.plot.barcode(
        barcode, color="b", new_fig=False, xlim=(0, 100), ylim=(0, 100), xlabel="", ylabel=""
    )
    ax2 = fig.add_subplot(323)
    tmd.view.plot.diagram(
        barcode, color="b", new_fig=False, xlim=(0, 100), ylim=(0, 100), xlabel="", ylabel=""
    )
    ax3 = fig.add_subplot(325)
    tmd.view.plot.persistence_image(
        barcode, new_fig=False, xlim=(0, 100), ylim=(0, 100), xlabel="", ylabel=""
    )
    ax4 = fig.add_subplot(122)
    tmd.view.view.neuron(
        morphology,
        new_fig=False,
        treecolors="b",
        subplot=(122),
        xlim=(-300, 300),
        ylim=(-1000, 1000),
        no_axes=True,
    )

    return fig
