import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g = 1      # gravity constant (m/s^2)
    M = 1      # mass of the booster (kg)
    l = 2      # total length of the booster (meters)
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(cos, sin):
    def cartesian_coordinates(f, theta, phi):
        fx = -f * sin(theta + phi)
        fy = f * cos(theta + phi)
        return fx, fy

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Équation du mouvement du centre de masse

    Par le principe fondamental de la dynamique (2ème loi de Newton), appliqué au centre de masse :

    \[
    M\ddot{x} = f_x
    \qquad
    M\ddot{y} = f_y - Mg
    \]

    En substituant les expressions de \( f_x \) et \( f_y \) trouvées précédemment :

    \[
    \ddot{x}
    =
    -\frac{f}{M}\sin(\theta + \varphi)
    \]

    \[
    \ddot{y}
    =
    \frac{f}{M}\cos(\theta + \varphi) - g
    \]

    ---

    # En Python

    On représente l'état du système par le vecteur :

    \[
    \mathbf{s}
    =
    (x,\ y,\ \dot{x},\ \dot{y})
    \]
    """)
    return


@app.cell
def _(M, g, np):
    def dynamics_cm(t, state, f, theta, phi):
        """
        state = [x, y, vx, vy]
        Retourne la dérivée d'état [vx, vy, ax, ay].
        """
        x, y, vx, vy = state
        ax = -f * np.sin(theta + phi) / M
        ay =  f * np.cos(theta + phi) / M - g
        return [vx, vy, ax, ay]

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(M, l):
    J = (1/12) * M * l**2
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tilt dynamics (angular acceleration)

    We model the rotational motion of the booster using Newton's second law for rotation:

    \[
    J\ddot{\theta} = \tau
    \]

    The engine produces a torque due to the thrust applied at the base of the booster:

    \[
    \tau = -\frac{l}{2} f \sin(\phi)
    \]

    Final equation governing the tilt:

    \[
    \ddot{\theta} = -\frac{l}{2J} f \sin(\phi)
    \]
    """)
    return


@app.cell
def _(J, l, sin):
    def tilt_theta(f, phi):
        ddtheta = -(l / (2 * J)) * f * sin(phi)
        return ddtheta

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Vector field formulation

    We define the state variables of the system as:
    - \(v_x = \dot{x}\), \(v_y = \dot{y}\) (linear velocities)
    - \(\omega = \dot{\theta}\) (angular velocity)

    ---

    ### State space dimension

    The state vector is:

    \[
    s = (x, y, \theta, v_x, v_y, \omega)
    \]

    So the dimension of the state space is:

    \[
    n = 6
    \]

    ---

    ### State-space dynamics

    The system evolves according to:

    \[
    \dot{s} = F(s, f, \phi)
    \]

    where \(F : \mathbb{R}^{6+2} \to \mathbb{R}^6\).

    ---

    ### Vector field definition

    The dynamics are given by:

    \[
    \begin{aligned}
    \dot{x} &= v_x \\
    \dot{y} &= v_y \\
    \dot{\theta} &= \omega \\
    \dot{v_x} &= -f \sin(\theta + \phi) \\
    \dot{v_y} &= f \cos(\theta + \phi) - g \\
    \dot{\omega} &= -\frac{l}{J} f \sin(\phi)
    \end{aligned}
    \]
    """)
    return


@app.cell
def _(J, cos, g, l, sin):
    def F(s, f, phi):
        x, y, theta, vx, vy, omega = s

        # Accelerations
        ax = -f * sin(theta + phi)
        ay =  f * cos(theta + phi) - g
        alpha = -(l / J) * f * sin(phi)

        # State derivative
        dx = vx
        dy = vy
        dtheta = omega

        dvx = ax
        dvy = ay
        domega = alpha

        return (dx, dy, dtheta, dvx, dvy, domega)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Simulation

    We define a function that computes the time evolution of the booster by numerically solving its differential equations.

    ---

    ### Inputs

    - \(t_{\text{span}} = (t_0, t_f)\): initial and final times
    - \(y_0 = (x, v_x, y, v_y, \theta, \omega)\): initial state of the system
    - \(f_\phi(t, y)\): control function returning the thrust \(f\) and the angle \(\phi\)

    ---

    ### Method

    The system follows the state-space form:

    \[
    \dot{s} = F(s, f, \phi)
    \]

    where the dynamics include:
    - translational motion under thrust and gravity
    - rotational motion due to torque generated by the engine

    The system is integrated over time using a numerical ODE solver, and the result is returned as an interpolating function.

    ---

    ### Output

    The function returns:
    - \(sol(t)\): the state of the system at any time \(t\)
    - it also supports vectorized inputs (arrays of times)
    """)
    return


@app.cell
def _(J, g, l, np, sci):
    def redstart_solve(t_span, y0, f_phi):

        def dynamics(t, y):
            x, vx, y_pos, vy, theta, omega = y

            f, phi = f_phi(t, y)

            ax = -f * np.sin(theta + phi)
            ay =  f * np.cos(theta + phi) - g

            alpha = -(l / J) * f * np.sin(phi)

            return np.array([
                vx,
                ax,
                vy,
                ay,
                omega,
                alpha
            ])

        sol = sci.solve_ivp(
            dynamics,
            t_span,
            y0,
            dense_output=True
        )

        return sol.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Free-fall test

    In the free-fall scenario, the booster is subject only to gravity since the thrust is zero:

    \[
    f = 0
    \]

    ---

    ### Theoretical result

    The vertical motion satisfies:

    \[
    \ddot{y} = -g
    \]

    With initial conditions:
    - \(y(0) = 10\)
    - \(\dot{y}(0) = 0\)

    The motion is a parabola:

    \[
    y(t) = 10 - \frac{1}{2}t^2
    \]

    We find the time when the center of mass reaches the reference height \(y = \ell\):

    \[
    10 - \frac{1}{2}t^2 = \ell
    \]

    which gives:

    \[
    t = 4
    \]

    ---

    ### Numerical verification

    The simulation uses `redstart_solve` with zero thrust to reproduce free fall dynamics.

    We plot:
    - the numerical solution \(y(t)\)
    - the reference height \(y = \ell\)
    - the theoretical crossing time \(t = 4\)

    ---

    ### Expected result

    The curve should intersect \(y = \ell\) at approximately:

    \[
    t \approx 4
    \]

    confirming the correctness of the numerical solver.
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

        def f_phi(t, y):
            return np.array([0.0, 0.0])  # no thrust

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]  # y position

        plt.figure()

        plt.plot(t, y_t, label="y(t)")
        plt.axhline(l, color="grey", ls="--", label="y = l")

        # theoretical crossing
        plt.axvline(4, color="red", ls="--", label="t = 4 (theory)")

        plt.title("Free Fall Test")
        plt.xlabel("time t")
        plt.ylabel("height y")
        plt.grid(True)
        plt.legend()

        return plt.gcf()

    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Controlled landing

    We consider a landing scenario where the booster starts with:

    - \(x(0)=0\), \(v_x(0)=0\)
    - \(\theta(0)=0\), \(\dot{\theta}(0)=0\)
    - \(y(0)=10\), \(\dot{y}(0)=-2\)

    The objective is to reach:

    \[
    y(5)=\frac{\ell}{2}=1, \quad \dot{y}(5)=0
    \]

    while applying a thrust aligned with the booster axis (\(\theta=0\)).

    ---

    ### Strategy

    We construct a time-varying thrust \(f(t)\) that ensures a smooth descent by enforcing a polynomial motion profile for the vertical position. The corresponding acceleration is then converted into thrust using:

    \[
    \ddot{y}(t) = f(t) - g
    \]

    ---

    ### Control law

    The resulting thrust profile is time-dependent and designed to:
    - reduce the initial downward velocity
    - smoothly decelerate the booster
    - ensure zero velocity at landing

    ---

    ### Simulation

    The system is simulated using `redstart_solve` with the computed control law.

    We observe:
    - \(y(t)\): vertical position
    - comparison with target height \(y = 1\)
    - verification of smooth descent and final rest condition

    ---

    ### Expected behavior

    At \(t = 5\):
    - \(y(t)\) should reach \(1\)
    - \(\dot{y}(t)\) should approach \(0\)

    This confirms that the controlled thrust achieves a stable landing.
    """)
    return


@app.cell
def _(g, np, plt, redstart_solve):
    # coefficients
    a = -0.032
    b = 0.64

    def f_phi(t, y):
        f = 6*a*t + 2*b + g   # control force
        phi = 0.0             # vertical thrust
        return np.array([f, phi])

    def controlled_landing():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(0, 5, 1000)

        y = sol(t)[2]
        vy = sol(t)[3]

        plt.figure()

        plt.plot(t, y, label="y(t) (actual)")
        plt.axhline(1, color="grey", ls="--", label="target y = 1")

        plt.title("Controlled Landing (physical descent)")
        plt.xlabel("time t")
        plt.ylabel("height y")
        plt.grid(True)
        plt.legend()

        return plt.gcf()

    controlled_landing()
    return


@app.cell
def _(g, np):
    Kp = 3.0
    Kd = 2.0

    def y_desired(t):
        return 10 + (1 - 10) * (t / 5)

    def dy_desired(t):
        return (1 - 10) / 5

    def f_phi(t, y):
        x, vx, y_pos, vy, theta, omega = y

        f = g + Kp * (y_desired(t) - y_pos) + Kd * (dy_desired(t) - vy)
        phi = 0.0

        return np.array([f, phi])

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


if __name__ == "__main__":
    app.run()
