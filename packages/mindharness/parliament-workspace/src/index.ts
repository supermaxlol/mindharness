/**
 * parliament-workspace — Global Workspace broadcast.
 * Bid = salience × utility × habit_strength × affect_gain
 * affect_gain in [0.5, 2.0] from AffectState.salience_multiplier()
 */

export type Bid = {
  name: string;
  salience: number;
  utility: number;
  habitStrength: number; // [0,1]
  affectGain: number;    // [0.5,2.0]
  content: string;
};

export function score(b: Bid): number {
  return b.salience * b.utility * b.habitStrength * b.affectGain;
}

export class Workspace {
  timeoutMs = 1500;

  compete(bids: Bid[]): { winner: Bid; broadcast: Array<unknown> } {
    if (!bids.length) throw new Error("workspace: no bids");
    const winner = [...bids].sort((a, b) => score(b) - score(a))[0];
    const broadcast = [{ name: winner.name, content: winner.content, bid: score(winner), provenance: { source: "model_prior", ref: `workspace-${winner.name}` } }];
    return { winner, broadcast };
  }
}

export default Workspace;
